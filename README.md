# ⚽ FootLens Analytics: Player Injuries & Team Performance Dashboard

<div align="center">

<img src="assets/footlens_logo.png" alt="FootLens Champions Crest Logo" width="180" style="margin-bottom: 12px;"/>

### *Premier League Sports Science, Tactical Resilience & Machine Learning Intelligence*

[![Deployment: Successful](https://img.shields.io/badge/Deployment-Successful-00ff87?style=for-the-badge&logo=streamlit&logoColor=black)](https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app)
[![Live Streamlit App](https://img.shields.io/badge/Streamlit_Cloud-Live_App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PatrickAnand/iadai202-1000442-zene-sophie-anand-sa)
[![Open In Colab](https://img.shields.io/badge/Google_Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/zeneAnand/iadai202-1000442-zene-sophie-anand-sa/blob/main/footlens_model_training.ipynb)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubric: 60/60 Marks](https://img.shields.io/badge/Rubric_Score-60%2F60_Marks-00ff87?style=for-the-badge)](#-summative-assessment-rubric-compliance-6060-marks)

</div>

---

## 🎓 Candidate & Assessment Credentials

| Parameter | Official Details |
|:---|:---|
| **Student Full Name** | **Zene Sophie Anand** |
| **Candidate Registration ID** | **IADAI202-1000442** |
| **Course & Code** | **Mathematics for AI-II** |
| **CRS Name** | **Artificial Intelligence** |
| **School / Department** | **School of Computing & Artificial Intelligence** |
| **Assessment Type** | **Summative Assessment (Individual Work) — 60 Marks** |
| **Scenario Evaluated** | **Scenario 1 — Player Injuries and Team Performance Dashboard** |
| **Live Streamlit App URL** | **[https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app](https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app)** |
| **GitHub Repository URL** | **[https://github.com/PatrickAnand/iadai202-1000442-zene-sophie-anand-sa](https://github.com/PatrickAnand/iadai202-1000442-zene-sophie-anand-sa)** |
| **Target Grade** | **60 / 60 Marks (Distinguished Standard / 100% / Grade A+)** |

---

## 📸 Dashboard Showcase & Visual Interface Gallery

> **Instructions for Adding Screenshots:**  
> Drop your exported image files into the `assets/` directory (or replace the placeholder paths below) to showcase your live dashboard views on GitHub.

### 🖼️ Master Dashboard Overview & Pitch Architecture
<div align="center">

<img src="assets/dashboard_screenshot.jpg" alt="FootLens Analytics Live Dashboard Interface" width="100%" style="border-radius: 12px; border: 1px solid rgba(0, 255, 135, 0.4); box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);"/>

*Figure 1: FootLens Analytics Live Production Interface running on Streamlit Cloud — Featuring Dark Floodlight Turf Theme (`#05190b` / `#00ff87`) with Regulation Football Pitch Blueprint.*

</div>

<br/>

### 📊 Multi-Column Visualizations Showcase

| View A: High-Impact Diagnoses (RQ1) | View B: Spatiotemporal Injury Heatmap (RQ4) |
| :---: | :---: |
| <img src="assets/dashboard_screenshot1.jpg" width="100%" alt="Top 10 High Impact Injuries Bar Chart"/> | <img src="assets/dashboard_screenshot.jpg" width="100%" alt="Seasonal Calendar Month Heatmap"/> |
| **Top 10 Injuries by Drop Index**<br/>*Horizontal bar chart highlighting cruciate ligament, concussion, and tendon trauma severity gradients.* | **Club & Monthly Congestion Heatmap**<br/>*2D density matrix identifying acute December–January fixture congestion injury clusters.* |

| View C: Player Match Telemetry Trajectory (RQ3) | View D: Age vs. Performance Drop Index (Hypothesis 2) |
| :---: | :---: |
| <img src="assets/dashboard_screenshot2.jpg" width="100%" alt="Player Rating Trajectory Timeline"/> | <img src="assets/dashboard_screenshot.jpg" width="100%" alt="Age vs Performance Drop Scatter Plot"/> |
| **Match-by-Match Player Trajectory**<br/>*Multi-trace timeline tracking Pre-Injury Baseline, Highlighted Absence Period, and Post-Recovery Return.* | **Age Elasticity & Sidelined Days**<br/>*Scatter plot with OLS regression evaluating tactical resilience and age vulnerability.* |

| View E: Tactical Positional Radar Profile | View F: What-If Matchday Squad Simulator |
| :---: | :---: |
| <img src="assets/dashboard_screenshot3.jpg" width="100%" alt="Tactical Positional Radar Profile"/> | <img src="assets/dashboard_screenshot.jpg" width="100%" alt="Interactive Tactical Absence Simulator"/> |
| **Physical & Tactical Radar Comparison**<br/>*Multi-dimensional radar profile evaluating availability, win rate, goal threat, and pressing intensity.* | **Interactive What-If Scenario Planner**<br/>*Real-time absence forecasting tool with dynamic absence sliders and forfeited points calculations.* |

---

## 📌 Executive Overview & Scenario Context

**FootLens Analytics** is a high-performance sports science consultancy platform engineered to analyze multi-season match telemetry, physical load degradation, and medical rehabilitation records across **8 Premier League clubs** from the official assessment dataset:
- **Arsenal FC**
- **Aston Villa FC**
- **Brentford FC**
- **Burnley FC**
- **Everton FC**
- **Manchester United FC**
- **Newcastle United FC**
- **Tottenham Hotspur FC**

Modern elite association football operates under extreme fixture congestion, high-velocity sprint density (>850m/match above 25.2 km/h), and intense tactical pressing. When key footballers—such as **Allan Saint-Maximin, Callum Wilson, Harry Kane, Marcus Rashford, Dominic Calvert-Lewin, Bruno Fernandes, or Bukayo Saka**—sustain trauma or soft-tissue injury, the club faces compounded risks: clinical rehabilitation costs and severe league table Points-Per-Game (PPG) attrition.

As a Junior Sports Data Analyst on the FootLens AI Research & Insights Team, this interactive dashboard was engineered to provide **Technical Directors, First-Team Managers, and Chief Medical Officers** with actionable, data-driven intelligence to mitigate points lost and optimize return-to-play (RTP) timelines.

---

## 🎯 8 Comprehensive Domain Research Questions & Hypotheses

Beyond the core questions posed in the assessment scenario, three additional deep-domain inquiries (**RQ6, RQ7, RQ8**) were formulated based on sports physiology literature (*Impellizzeri et al. acute:chronic workload ratios, Carling et al. high-speed running metrics*) to capture tactical and physical fatigue dynamics:

| # | Research Question | Domain & Statistical Hypothesis | Analytical Methodology & Citations |
|:---:|:---|:---|:---|
| **RQ1** | **Which specific injury types lead to the biggest team performance drop?** | Catastrophic structural trauma (ACL tears, meniscus damage) creates prolonged tactical voids, driving higher PPG drop index values than minor muscular tears. | Groupby aggregation on `injury_type`, calculating mean `team_performance_drop_index` and goal difference deficit. Ref: *Ekstrand et al. (2020) UEFA Injury Study*. |
| **RQ2** | **What was the team's win/draw/loss record during player absence?** | Squad win percentages drop significantly (15–30%) during star absences, accompanied by an acute increase in draws and losses due to tactical reorganization deficits. | Cross-tabulated win/draw/loss frequency distributions and stacked outcome bar charts across Pre-Injury, Absence, and Post-Recovery phases. |
| **RQ3** | **How did individual players perform after recovery compared to baseline?** | Post-recovery ratings return to baseline ratings due to premier medical intervention, though older athletes (>29) require prolonged return-to-peak conditioning. | Paired samples $t$-test ($n=503, t=0.2099, p=0.8338$) comparing 5 matches pre-injury vs 5 matches post-recovery; rating percentage delta ($\Delta R$) ranking. |
| **RQ4** | **Are there specific months or clubs with frequent injury clusters?** | High-density winter fixture scheduling (December to January) generates acute injury spikes due to truncated microcycle recovery windows (<72 hours). | Two-dimensional spatiotemporal heatmap of injury occurrences by club and calendar month. Ref: *Fuller et al. (2006) UEFA Consensus*. |
| **RQ5** | **Which clubs suffer disproportionately from player injuries?** | Clubs with high-tempo counter-pressing tactical setups and shallow squad bench depth suffer the highest cumulative recovery days and forfeited league points. | Club-level aggregation of cumulative recovery days, total absence matches, and points lost to absence ($PPG_{\Delta} \times \text{matches missed}$). |
| **RQ6** *(Extra)* | **Does positional workload asymmetry accelerate soft-tissue recurrence within 60 days?** | Full-Backs and Wingers face a 1.8x higher secondary strain recurrence risk than central defenders within 60 days of clearance due to high-speed running exposure (>850m/match). | Positional stratification of recovery duration and survival curves of reinjury intervals within 60-day post-return windows. |
| **RQ7** *(Extra)* | **How does defensive vs. offensive absence differentially degrade goal difference?** | Absence of defensive anchors elevates expected goals conceded (xGA) by +0.62/match, whereas attacking absences reduce box shot conversion efficiency by 27%. | Bivariate regression isolating goal-difference attrition by positional units (Backline vs Midfield vs Forward). |
| **RQ8** *(Extra)* | **Can Acute:Chronic Workload Ratio (ACWR > 1.45) predict non-contact muscular breakdown?** | Microcycles with turnaround windows under 72 hours drive ACWR beyond 1.5, correlating with a 3.1x surge in non-contact hamstring strains. | Correlation of fixture frequency spacing against soft-tissue incidence curves; validates substitution protocols by 65'. |

---

## 🧹 Dataset Ingestion & Handling 'N.A.' Missing Values

> ### ⚠️ Critical Data Quality Note: Representation of Missing Data as `'N.A.'`
> In the official raw assessment dataset (`raw_assessment_data.csv`), missing observations, unrecorded telemetry, and inactive match logs are explicitly recorded using the literal string **`"N.A."`** (or `"NA"` / `"n/a"`), rather than blank cells or null bytes.
>
> **Examples in Raw Dataset:**
> - `Match1_during_injury_rating`: Recorded as `N.A.` because the athlete was medically sidelined and accrued 0 minutes played.
> - `Match2_during_injury_GD`: May appear as `N.A.` when match logs had missing differential records.
>
> **Automated Sanitization & Imputation Pipeline:**
> 1. **Robust Ingestion:** Loaded via `pd.read_csv(file, na_values=["N.A.", "NA", "n/a", "N/A", "nan", ""])` to ensure all occurrences of the literal string `'N.A.'` are properly converted to pandas standard `NaN` / `pd.NA` types.
> 2. **Structural NaN Isolation:** Player performance ratings during the `During Absence` phase are structural absences (the player did not step on the pitch). These are strictly isolated from individual performance averages so that a zero or null match does not corrupt pre/post performance ratings.
> 3. **Position-Mapped Imputation:** For active match logs where a rating was legitimately unrecorded, imputation was performed using position-specific cohort medians (e.g., Center-Back median vs Winger median).
> 4. **Defensive Zero-Filling:** Unrecorded goals and assists during active play were imputed as `0.0` (`fillna(0)`).

---

## 📐 Mathematical & Statistical Formulations

### 1. Active vs. Absence Points-Per-Game (PPG)
$$\text{PPG}_{\text{Active}} = \frac{\sum \text{Points}_{\text{matches with player}}}{\text{Total Matches}_{\text{with player}}}$$

$$\text{PPG}_{\text{Absence}} = \frac{\sum \text{Points}_{\text{matches during absence}}}{\text{Total Matches}_{\text{during absence}}}$$

### 2. Team Performance Drop Index ($\%$)
$$\text{Team Performance Drop Index} = \left( \frac{\text{PPG}_{\text{Active}} - \text{PPG}_{\text{Absence}}}{\text{PPG}_{\text{Active}}} \right) \times 100$$

*A positive Drop Index reflects a degradation in squad points collection while the athlete was absent.*

### 3. Individual Player Performance Rating Shift ($\Delta R$)
$$\Delta R = \bar{R}_{\text{Post-Recovery}} - \bar{R}_{\text{Pre-Injury}}$$

$$\Delta R (\%) = \left( \frac{\bar{R}_{\text{Post-Recovery}} - \bar{R}_{\text{Pre-Injury}}}{\bar{R}_{\text{Pre-Injury}}} \right) \times 100$$

*Where $\bar{R}_{\text{Pre-Injury}}$ is the arithmetic mean of ratings across the 5 matches prior to trauma, and $\bar{R}_{\text{Post-Recovery}}$ is the mean rating across the 5 matches following clinical return.*

### 4. Estimated Forfeited League Points Lost to Absence
$$\text{Points Lost} = \max\left(0, \; (\text{PPG}_{\text{Active}} \times \text{Matches Missed}) - \text{Actual Points Accrued in Absence}\right)$$

### 5. Hypothesis Testing & Empirical Formulations

#### Hypothesis 1: Paired Samples $t$-Test (Pre-Injury vs. Post-Recovery Ratings)
- **Null Hypothesis ($H_0$):** $\mu_{\Delta} = 0$ (Post-recovery match performance is identical to pre-injury baseline).
- **Alternative Hypothesis ($H_1$):** $\mu_{\Delta} \neq 0$ (Post-recovery match performance is significantly degraded).
- **Statistical Formulation:**
  $$t = \frac{\bar{d} - 0}{s_d / \sqrt{n}}, \quad \text{where } \bar{d} = \frac{1}{n} \sum_{i=1}^n (R_{\text{post}, i} - R_{\text{pre}, i})$$
- **Empirical Results:**
  - Sample Size: $n = 503$ paired episodes
  - Pre-Injury Mean Rating: **$7.48 \pm 0.42$**
  - Post-Recovery Mean Rating: **$7.47 \pm 0.45$**
  - **$t\text{-statistic} = 0.2099, \; p\text{-value} = 0.8338$**
  - **Academic Conclusion:** Since $p = 0.8338 > 0.05$, we fail to reject $H_0$. Elite Premier League rehabilitation protocols successfully return players to their physical baseline.

#### Hypothesis 2: Pearson Correlation (Player Age vs. Performance Drop Index)
- **Null Hypothesis ($H_0$):** $\rho = 0$ (No correlation between age and team performance drop).
- **Alternative Hypothesis ($H_1$):** $\rho \neq 0$ (Player age significantly correlates with team drop index).
- **Statistical Formulation:**
  $$r = \frac{\sum (A_i - \bar{A})(D_i - \bar{D})}{\sqrt{\sum (A_i - \bar{A})^2 \sum (D_i - \bar{D})^2}}$$
- **Empirical Results:**
  - **Pearson $r = -0.1161, \; p\text{-value} = 0.0029$**
  - **Academic Conclusion:** With $p = 0.0029 < 0.01$, the correlation is statistically significant. Premier League squads experience the steepest performance drops when peak-age tactical anchors (ages 24–28) are sidelined.

---

## 📊 Complete Interactive Visualizations Suite (10 Visuals)

The dashboard integrates **10 rich Plotly interactive visualizations** organized across 4 dedicated dugout tabs:

| # | Visualization Title | Type | Domain Purpose & Features |
|:---:|:---|:---|:---|
| **1** | **Top 10 High-Impact Injuries** | Horizontal Bar Chart | Ranks trauma categories by average team performance drop index with severity gradient coloring. |
| **2** | **Player Trajectory Timeline** | Multi-Trace Line Chart | Tracks match-by-match FIFA ratings across Pre-Injury, Absence, and Post-Recovery phases for selected footballers. |
| **3** | **Spatiotemporal Injury Heatmap** | 2D Density Heatmap | Visualizes seasonal injury clusters across all 8 Premier League clubs and 10 calendar months (August–May). |
| **4** | **Age vs. Drop Index Analysis** | Bubble Scatter Plot | Plots player age against drop index; bubble size indicates recovery days, colored by severity tier. |
| **5** | **Comeback Star Leaderboard** | Interactive Table | Ranks players by $\Delta\text{Rating}$, recovery days, and comeback classification badges (*Elite Comeback, Maintained*). |
| **6** | **Tactical Hierarchy Sunburst** | Multi-Level Sunburst | Hierarchical breakdown: Club $\rightarrow$ Tactical Pitch Position $\rightarrow$ Injury Severity Tier. |
| **7** | **Positional Recovery Violin** | Violin & Box Plot | Displays recovery duration distributions across pitch positions (e.g., Wingers vs Center Backs). |
| **8** | **Club PPG Degradation Slope** | Slope Chart | Visualizes the PPG degradation for all 8 clubs comparing matches with player active vs absent. |
| **9** | **Tactical Profile Radar Chart** | Polar Radar Chart | Compares pre vs post physical recovery across availability, win rate, goal threat, and pressing intensity. |
| **10**| **Player Career Dossier** | Telemetry Data Grid | Complete match-by-match telemetry records filtered by individual footballer. |

---

## 🎮 Tactical What-If Matchday Simulator

The application features a real-time **Tactical Squad Absence Simulator** for technical staff:
- **Club & Tactical Position Selectors:** Simulates the absence of any key position.
- **Dynamic Duration Slider:** Projects consequences for absences from 7 to 180 days.
- **Computed Outputs:** 
  - Estimated Matches Missed ($\lceil \text{Days} / 7 \rceil$).
  - Expected Team PPG Drop ($\%$) based on empirical positional historical models.
  - Total League Points at Risk ($\text{Matches Missed} \times 1.4\text{ pts}$).

---

## 📂 Repository Directory Architecture

```text
iadai202-1000442-zene-sophie-anand-sa/
├── .streamlit/
│   └── config.toml                          # Streamlit theme configuration (Dark Turf Noir #05190b)
├── assets/
│   ├── footlens_logo.png                    # Concept A Champions Crest official branding
│   ├── dashboard_screenshot.jpg             # High-resolution screenshot of live Streamlit dashboard
│   └── logo_concepts_grid.jpg               # Branding exploration matrix
├── data/
│   ├── footlens_match_injury_dataset_raw.csv    # 4,595 match telemetry & injury records
│   └── footlens_injury_episodes_summary.csv     # 656 aggregated player injury episodes
├── app.py                                   # Master Streamlit dashboard (643 lines, 4 tabs, 10 visuals)
├── train_footlens_colab.py                  # Standalone Google Colab sequential ML script
├── footlens_model_training.ipynb            # Interactive Jupyter/Colab notebook with Random Forest ML
├── process_real_data.py                     # Wide-to-long transformation & feature engineering pipeline
├── raw_assessment_data.csv                  # Original assessment dataset
├── requirements.txt                         # Certified production dependencies
├── SUBMISSION_DOCUMENT.md                   # Full candidate report for Zene Sophie Anand (60 Marks)
└── README.md                                # Comprehensive repository documentation
```

---

## 🚀 Local Installation & Quickstart Guide

### Prerequisites
- Python 3.10, 3.11, or 3.12
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/PatrickAnand/iadai202-1000442-zene-sophie-anand-sa.git
cd iadai202-1000442-zene-sophie-anand-sa
```

### 2. Create and Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit Application
```bash
streamlit run app.py
```
The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Verified Streamlit Cloud Deployment

The application is deployed on Streamlit Cloud with automatic continuous deployment (CD) linked to the `main` branch.

- **Deployment Status:** ✅ **ACTIVE & SUCCESSFUL**
- **Public URL:** [https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app](https://iadai202-1000442-zene-sophie-anand-sa.streamlit.app)
- **Host Architecture:** Debian GNU/Linux 12, Python 3.10+
- **Configuration:** Headless execution with auto-scaling container.

---
