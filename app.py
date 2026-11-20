

import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, classification_report, accuracy_score

try:
    from google.colab import files
    print("📁 Upload 'player_injuries_impact.csv' or 'raw_assessment_data.csv':")
    uploaded = files.upload()
    uploaded_filename = list(uploaded.keys())[0] if uploaded else None
except Exception:
    uploaded_filename = None

if not uploaded_filename or not os.path.exists(uploaded_filename):
    for candidate in ["raw_assessment_data.csv", "player_injuries_impact.csv", "data/raw_assessment_data.csv"]:
        if os.path.exists(candidate):
            uploaded_filename = candidate
            break

print(f"\n✅ Active Dataset Loaded: {uploaded_filename}")
raw_df = pd.read_csv(uploaded_filename)
print(f"📊 Dataset Dimensions: {raw_df.shape[0]} rows, {raw_df.shape[1]} columns")

def clean_player_rating(val):
    if pd.isna(val) or str(val).strip() in ["N.A.", "nan", ""]:
        return np.nan
    s = re.sub(r"[^0-9.]", "", str(val))
    try:
        f = float(s)
        return f if 1.0 <= f <= 10.0 else np.nan
    except:
        return np.nan

def clean_match_outcome(val):
    if pd.isna(val) or str(val).strip() in ["N.A.", "nan", ""]:
        return "Draw"
    s = str(val).strip().capitalize()
    if "Win" in s: return "Win"
    elif "Lose" in s or "Loss" in s: return "Loss"
    return "Draw"

df_clean = raw_df.rename(columns={
    "Player_Name": "player_name",
    "Player_Age": "player_age",
    "Player_Position": "position",
    "Team_Name": "club",
    "injury_type": "injury_type",
    "injury_start_date": "injury_start_date",
    "injury_end_date": "injury_end_date",
    "Fifa_rating": "fifa_rating"
}).copy()

df_clean["injury_start_date"] = pd.to_datetime(df_clean["injury_start_date"], errors="coerce")
df_clean["injury_end_date"]   = pd.to_datetime(df_clean["injury_end_date"], errors="coerce")
df_clean["recovery_days"]     = (df_clean["injury_end_date"] - df_clean["injury_start_date"]).dt.days.clip(lower=1)
df_clean["injury_month"]      = df_clean["injury_start_date"].dt.strftime("%B")

df_clean["player_age"]  = pd.to_numeric(df_clean["player_age"], errors="coerce").fillna(df_clean["player_age"].median())
df_clean["fifa_rating"] = pd.to_numeric(df_clean["fifa_rating"], errors="coerce").fillna(df_clean["fifa_rating"].median())

def assign_severity_tier(days):
    if days <= 7: return "Minor"
    elif days <= 28: return "Moderate"
    return "Severe"

df_clean["severity_tier"] = df_clean["recovery_days"].apply(assign_severity_tier)

pre_cols  = [c for c in df_clean.columns if "before_injury_Player_rating" in c]
post_cols = [c for c in df_clean.columns if "after_injury_Player_rating" in c]

df_clean["pre_injury_avg_rating"]  = df_clean[pre_cols].map(clean_player_rating).mean(axis=1).round(2)
df_clean["post_injury_avg_rating"] = df_clean[post_cols].map(clean_player_rating).mean(axis=1).round(2)

cohort_pre_medians = df_clean.groupby("position")["pre_injury_avg_rating"].transform("median")
df_clean["pre_injury_avg_rating"]  = df_clean["pre_injury_avg_rating"].fillna(cohort_pre_medians).fillna(6.40)
df_clean["post_injury_avg_rating"] = df_clean["post_injury_avg_rating"].fillna(df_clean["pre_injury_avg_rating"])

df_clean["rating_delta"]      = (df_clean["post_injury_avg_rating"] - df_clean["pre_injury_avg_rating"]).round(2)
df_clean["rating_pct_change"] = ((df_clean["rating_delta"] / df_clean["pre_injury_avg_rating"]) * 100.0).round(2)

def classify_trajectory(delta):
    if delta >= 0.50: return "Elite Comeback"
    elif delta <= -0.50: return "Performance Decline"
    return "Baseline Recovery"

df_clean["recovery_trajectory"] = df_clean["rating_delta"].apply(classify_trajectory)

during_res_cols = [c for c in df_clean.columns if "during_injury_match_outcome" in c]
pts_map = {"Win": 3, "Draw": 1, "Loss": 0}

def calc_absence_ppg(row):
    pts, cnt = 0, 0
    for col in during_res_cols:
        val = str(row[col])
        if pd.notna(row[col]) and val not in ["nan", "N.A."]:
            res = clean_match_outcome(val)
            pts += pts_map[res]
            cnt += 1
    return (pts / cnt) if cnt > 0 else 1.30

df_clean["team_ppg_during_absence"] = df_clean.apply(calc_absence_ppg, axis=1).round(2)
fifa_norm = (df_clean["fifa_rating"] - 65.0) / 25.0
df_clean["team_ppg_with_player"] = (1.40 + 0.80 * fifa_norm).clip(1.20, 2.60).round(2)

df_clean["team_performance_drop_index"] = (
    ((df_clean["team_ppg_with_player"] - df_clean["team_ppg_during_absence"]) / df_clean["team_ppg_with_player"]) * 100.0
).clip(lower=0.0).round(2)

match_rows = []
for idx, row in df_clean.iterrows():
    p_name = row["player_name"]
    p_club = row["club"]
    p_pos  = row["position"]
    p_age  = row["player_age"]
    dur    = row["recovery_days"]
    st_dt  = row["injury_start_date"]
    end_dt = row["injury_end_date"]
    
    for i, col in enumerate(pre_cols):
        r_val = clean_player_rating(row[col])
        if pd.notna(r_val):
            m_date = st_dt - pd.Timedelta(days=7 * (len(pre_cols) - i))
            match_rows.append({
                "match_id": f"PRE_{idx}_{i+1}",
                "player_name": p_name,
                "club": p_club,
                "position": p_pos,
                "player_age": p_age,
                "injury_phase": "Pre-Injury",
                "match_date": m_date,
                "player_performance_rating": r_val,
                "match_result": "Win" if r_val >= 7.0 else ("Draw" if r_val >= 6.0 else "Loss"),
                "goal_difference": 1 if r_val >= 7.0 else (0 if r_val >= 6.0 else -1),
                "injury_type": row["injury_type"],
                "recovery_days": dur,
                "severity_tier": row["severity_tier"]
            })
            
    for j, col in enumerate(during_res_cols):
        res_raw = row[col]
        if pd.notna(res_raw) and str(res_raw) not in ["nan", "N.A."]:
            res = clean_match_outcome(res_raw)
            m_date = st_dt + pd.Timedelta(days=max(1, int(dur * (j + 1) / (len(during_res_cols) + 1))))
            match_rows.append({
                "match_id": f"ABS_{idx}_{j+1}",
                "player_name": p_name,
                "club": p_club,
                "position": p_pos,
                "player_age": p_age,
                "injury_phase": "During Absence",
                "match_date": m_date,
                "player_performance_rating": np.nan,
                "match_result": res,
                "goal_difference": 2 if res == "Win" else (0 if res == "Draw" else -2),
                "injury_type": row["injury_type"],
                "recovery_days": dur,
                "severity_tier": row["severity_tier"]
            })
            
    for k, col in enumerate(post_cols):
        r_val = clean_player_rating(row[col])
        if pd.notna(r_val):
            m_date = end_dt + pd.Timedelta(days=7 * (k + 1))
            match_rows.append({
                "match_id": f"POST_{idx}_{k+1}",
                "player_name": p_name,
                "club": p_club,
                "position": p_pos,
                "player_age": p_age,
                "injury_phase": "Post-Recovery",
                "match_date": m_date,
                "player_performance_rating": r_val,
                "match_result": "Win" if r_val >= 7.0 else ("Draw" if r_val >= 6.0 else "Loss"),
                "goal_difference": 1 if r_val >= 7.0 else (0 if r_val >= 6.0 else -1),
                "injury_type": row["injury_type"],
                "recovery_days": dur,
                "severity_tier": row["severity_tier"]
            })

df_match_logs = pd.DataFrame(match_rows)
print(f"✅ Match Logs Created: {len(df_match_logs):,} rows across 3 phases.")

pre_ratings  = df_clean["pre_injury_avg_rating"].dropna()
post_ratings = df_clean["post_injury_avg_rating"].dropna()
common_idx   = pre_ratings.index.intersection(post_ratings.index)

diff = pre_ratings.loc[common_idx] - post_ratings.loc[common_idx]
diff_mean = diff.mean()
diff_std  = diff.std(ddof=1)
n_pairs   = len(diff)
t_stat, p_val = stats.ttest_rel(pre_ratings.loc[common_idx], post_ratings.loc[common_idx])

print("\n" + "=" * 80)
print(f"Paired t-Test: t = {t_stat:.4f}, p = {p_val:.4f} (n = {n_pairs} pairs)")
corr_data = df_clean[["recovery_days", "team_performance_drop_index"]].dropna()
r_val, p_corr = stats.pearsonr(corr_data["recovery_days"], corr_data["team_performance_drop_index"])
print(f"Pearson Correlation (Days vs Drop): r = {r_val:+.4f}, p = {p_corr:.4f}")
print("=" * 80)

feature_cols = ["player_age", "fifa_rating", "recovery_days", "pre_injury_avg_rating"]
df_ml = df_clean.dropna(subset=feature_cols + ["team_performance_drop_index", "recovery_trajectory"]).copy()

X = pd.get_dummies(df_ml[feature_cols + ["club", "position"]], drop_first=True)
y_reg = df_ml["team_performance_drop_index"]

X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.20, random_state=42)

rf_reg = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
rf_reg.fit(X_train, y_train_reg)

y_pred_reg = rf_reg.predict(X_test)
print(f"\nRandom Forest Regressor R²: {r2_score(y_test_reg, y_pred_reg):.4f}")
print(f"MAE: {mean_absolute_error(y_test_reg, y_pred_reg):.4f}% drop")

# Export preprocessed CSV files for the Streamlit dashboard
df_clean.to_csv("footlens_injury_episodes_summary.csv", index=False)
df_match_logs.to_csv("footlens_match_injury_dataset_raw.csv", index=False)
print("\n✅ Successfully exported:")
print("  • 'footlens_injury_episodes_summary.csv'")
print("  • 'footlens_match_injury_dataset_raw.csv'")
