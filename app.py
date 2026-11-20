"""
FootLens Analytics — Player Injuries and Team Performance Dashboard
Summative Assessment: Mathematics for AI-II | Artificial Intelligence
Author: Junior Sports Data Analyst, AI Research & Insights Team
Deployment: Streamlit Cloud | Engine: Python, Pandas, NumPy, Plotly, SciPy
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="FootLens Analytics | Player Injuries & Team Performance",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN SYSTEM & MODERN DARK THEME CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .main { background-color: #090d16; color: #e2e8f0; }
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 50%, rgba(15, 23, 42, 0.98) 100%);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 18px; padding: 26px 32px; margin-bottom: 24px;
    }
    .kpi-card {
        background: linear-gradient(145deg, #111827 0%, #0d131f 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px; padding: 18px 20px;
    }
    .kpi-label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #94a3b8; }
    .kpi-value { font-size: 1.85rem; font-weight: 800; color: #ffffff; }
</style>
""", unsafe_allow_html=True)

# 3. PREPROCESSING PIPELINE WITH CACHING
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RAW_PATH = os.path.join(DATA_DIR, "footlens_match_injury_dataset_raw.csv")

@st.cache_data(show_spinner=False)
def load_and_preprocess_data(uploaded_file=None):
    raw_df = pd.read_csv(uploaded_file if uploaded_file else RAW_PATH)
    raw_df.columns = [c.strip().lower().replace(" ", "_") for c in raw_df.columns]
    
    # Datetime conversions
    for c in ["match_date", "injury_start_date", "injury_end_date"]:
        if c in raw_df.columns: raw_df[c] = pd.to_datetime(raw_df[c], errors="coerce")
        
    # Handling missing values
    if "goals_scored" in raw_df.columns: raw_df["goals_scored"] = raw_df["goals_scored"].fillna(0)
    if "assists" in raw_df.columns: raw_df["assists"] = raw_df["assists"].fillna(0)
    
    # Impute missing active ratings with position cohort mean
    if "player_performance_rating" in raw_df.columns and "position" in raw_df.columns:
        active_mask = raw_df["injury_phase"] != "During Absence"
        raw_df.loc[active_mask & raw_df["player_performance_rating"].isna(), "player_performance_rating"] = \
            raw_df[active_mask].groupby("position")["player_performance_rating"].transform("mean")
            
    # Feature Engineering across injury episodes
    episodes = []
    for inj_id, g in raw_df.groupby("injury_id"):
        first = g.iloc[0]
        pre_g = g[g["injury_phase"] == "Pre-Injury"]
        abs_g = g[g["injury_phase"] == "During Absence"]
        post_g = g[g["injury_phase"] == "Post-Recovery"]
        with_g = g[g["injury_phase"] != "During Absence"]
        
        pre_rat = pre_g["player_performance_rating"].mean() if len(pre_g) > 0 else np.nan
        post_rat = post_g["player_performance_rating"].mean() if len(post_g) > 0 else np.nan
        rat_delta = post_rat - pre_rat if pd.notnull(pre_rat) and pd.notnull(post_rat) else 0.0
        rat_pct = (rat_delta / pre_rat * 100) if pd.notnull(pre_rat) and pre_rat > 0 else 0.0
        
        ppg_with = with_g["team_points"].mean() if len(with_g) > 0 else 0.0
        ppg_abs = abs_g["team_points"].mean() if len(abs_g) > 0 else 0.0
        drop_idx = max(-25.0, min(100.0, ((ppg_with - ppg_abs) / ppg_with * 100) if ppg_with > 0 else 0.0))
        
        w_abs = (abs_g["match_result"] == "Win").sum()
        d_abs = (abs_g["match_result"] == "Draw").sum()
        l_abs = (abs_g["match_result"] == "Loss").sum()
        
        trajectory = "Elite Comeback" if rat_pct >= 4.0 else ("Maintained Baseline" if rat_pct >= -1.5 else ("Slight Decline" if rat_pct >= -6.0 else "Severe Decline"))
        points_lost = max(0.0, (ppg_with * len(abs_g)) - abs_g["team_points"].sum())
        
        episodes.append({
            "injury_id": inj_id, "player_name": first["player_name"], "club": first["club"],
            "position": first["position"], "player_age": first["player_age"], "injury_type": first["injury_type"],
            "severity_tier": first["severity_tier"], "recovery_days": first["recovery_days"],
            "pre_injury_avg_rating": round(pre_rat, 2), "post_injury_avg_rating": round(post_rat, 2),
            "rating_delta": round(rat_delta, 2), "rating_pct_change": round(rat_pct, 2),
            "recovery_trajectory": trajectory, "team_ppg_with_player": round(ppg_with, 2),
            "team_ppg_during_absence": round(ppg_abs, 2), "team_performance_drop_index": round(drop_idx, 2),
            "absence_record_wdl": f"{w_abs}W-{d_abs}D-{l_abs}L", "points_lost_to_absence": round(points_lost, 1),
            "injury_start_date": first["injury_start_date"], "injury_end_date": first["injury_end_date"],
            "injury_month": first["injury_start_date"].strftime("%B") if pd.notnull(first["injury_start_date"]) else "Unknown"
        })
    return raw_df, pd.DataFrame(episodes)

# Load data and render Sidebar Filters, Hero Banner, 5 KPI Cards, and 6 Tabs
# (See full code in /footlens_sports_analytics/app.py)
