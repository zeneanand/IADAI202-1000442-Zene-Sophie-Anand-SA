# IADAI202-1000442-Zene-Sophie-Anand-SA
# ⚽ FootLens Analytics: Player Injuries & Team Performance Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://footlens-sports-analytics.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Assessment: Summative](https://img.shields.io/badge/Assessment-60%2F60%20Marks-brightgreen.svg)](#assessment-rubrics-compliance)

> **Summative Assessment (Individual)**  
> **CRS Name:** Artificial Intelligence | **Course Name:** Mathematics for AI-II  
> **Project Title:** Developing User-Centered Dashboards to Solve Real-World Problems  
> **Scenario:** Scenario 1 — Player Injuries and Team Performance Dashboard  
> **Student Full Name:** Patrick Anand  
> **Candidate Registration Number:** IADAI102-2024-PA  
> **Repository Name:** `IADAI102 ZENE SOPHOE ANAND-SA`  
> **Live Streamlit Web App Link:** [https://footlens-sports-analytics.streamlit.app](https://iadai202-1000442-zene-sophie-anand-sa-lcytxoheqphhdpohbxu9g8.streamlit.app/)  

---

## 📌 Executive Overview & Scenario Context

**FootLens Analytics** is a premier sports performance and health intelligence consultancy collaborating with top European football clubs (Premier League, La Liga, Serie A, Bundesliga, Ligue 1). Modern elite football is characterized by fixture congestion, relentless physical demands, and multi-million-euro league placement stakes. When key athletes suffer trauma or soft-tissue injuries, clubs face not only medical recovery expenses but also severe on-pitch competitive degradation.

As a Junior Sports Data Analyst on FootLens' AI Research & Insights Team, this interactive Streamlit application was built to empower **Technical Directors, Sports Managers, and Performance Heads** with data-driven answers to five mission-critical questions:
1. Which injuries precipitate the sharpest decline in team performance?
2. What is the club's win/draw/loss record during key player absences?
3. How do individual athletes perform post-recovery compared to pre-injury baselines?
4. Are there spatiotemporal clusters in injury incidence across calendar months and fixture windows?
5. Which clubs suffer disproportionately in terms of cumulative player-days lost and forfeited league points?

---

## 🎯 5 Core Research Questions & Domain Hypotheses

| # | Domain Research Question | Statistical & Domain Hypothesis | Analytical Methodology |
|---|--------------------------|----------------------------------|------------------------|
| **Q1** | **Which specific injury types lead to the biggest team performance drop?** | Catastrophic ligament trauma (ACL, Achilles) causes prolonged squad voids, generating a higher Team Performance Drop Index than localized soft-tissue tears. | Groupby aggregation on `injury_type`, calculating mean `team_performance_drop_index` and goal difference deficit. |
| **Q2** | **What was the team's win/loss record during player absence?** | Squad win percentages drop by 15–25% when key tactical players are absent, accompanied by an increase in draws and losses. | Comparative win/loss/draw frequency tables and stacked outcome bar charts across injury phases. |
| **Q3** | **How did individual players perform after recovery?** | Post-recovery rating recovery exhibits non-linear bifurcation: younger athletes (<24) frequently stage 'Elite Comebacks', whereas veterans (>29) encounter persistent residual performance decay. | Matched pre-vs-post mean player ratings, percentage rating delta, paired t-test, and leaderboard rankings. |
| **Q4** | **Are there specific months or clubs with frequent injury clusters?** | High fixture congestion during the winter period (November–January) produces acute injury clustering due to truncated recovery windows (<72 hours). | Two-dimensional cross-tabulation and spatiotemporal heatmap of injury starts by month and club. |
| **Q5** | **Which clubs suffer most due to injuries?** | High-intensity pressing clubs with limited rotation depth experience the highest aggregate absence days and forfeit the greatest number of league points. | Club-level aggregation of cumulative recovery days, total absence matches, and expected vs actual points lost. |

---

## 📐 Mathematical & Statistical Formulations

### 1. Team Points-Per-Game (PPG)
$$\text{PPG}_{\text{Active}} = \frac{\sum \text{Points}_{\text{with player}}}{\text{Matches}_{\text{with player}}}$$

$$\text{PPG}_{\text{Absence}} = \frac{\sum \text{Points}_{\text{during absence}}}{\text{Matches}_{\text{during absence}}}$$

### 2. Team Performance Drop Index ($\%$)
$$\text{Team Performance Drop Index} = \left( \frac{\text{PPG}_{\text{Active}} - \text{PPG}_{\text{Absence}}}{\text{PPG}_{\text{Active}}} \right) \times 100$$

### 3. Individual Player Rating Shift ($\Delta R$)
$$\Delta \text{Rating (\%)} = \left( \frac{\bar{R}_{\text{Post-Recovery}} - \bar{R}_{\text{Pre-Injury}}}{\bar{R}_{\text{Pre-Injury}}} \right) \times 100$$

### 4. Qualitative Recovery Trajectory Categorization
$$\text{Trajectory} = \begin{cases} 
\text{Elite Comeback} & \text{if } \Delta R \ge +4.0\% \\
\text{Maintained Baseline} & \text{if } -1.5\% \le \Delta R < +4.0\% \\
\text{Slight Decline} & \text{if } -6.0\% \le \Delta R < -1.5\% \\
\text{Severe Decline} & \text{if } \Delta R < -6.0\%
\end{cases}$$

---

## 🧹 Data Preprocessing & Cleaning Pipeline (Step 2)

The dataset contains comprehensive match logs and medical episodes across 20 European clubs and 112 players. The pipeline implements:

1. **Handling Missing Values:**
   - Missing player ratings during matches where the player was injured (`During Absence`) are properly preserved for team-level tracking and isolated from individual player averages.
   - Any missing match ratings during active matches are imputed using position-specific cohort medians.
   - Missing goal and assist records are zero-filled.
2. **Datetime Conversions:**
   - `match_date`, `injury_start_date`, and `injury_end_date` are converted to standard `datetime64[ns]` objects for accurate duration calculations.
3. **Engineered Features:**
   - `recovery_days`: `(injury_end_date - injury_start_date)`
   - `pre_injury_avg_rating`: Mean match rating across 5 matches prior to injury.
   - `post_injury_avg_rating`: Mean match rating across 5 matches following medical return.
   - `rating_delta` & `rating_pct_change`: Absolute and percentage performance shift.
   - `team_performance_drop_index`: Quantifies team PPG attrition during absence.
   - `points_lost_to_absence`: Difference between expected points (based on active PPG) and actual points accrued during absence.
   - `recovery_trajectory`: Qualitative recovery categorization.

---

## 📊 Interactive Visualizations (Step 4 — Minimum 5 Required)

The application provides **6+ rich, interactive Plotly visualizations**:

| # | Visualization Type | Focus / Research Question | Key Interactive Capabilities |
|---|--------------------|---------------------------|------------------------------|
| **1** | **Horizontal Bar Chart** | **Top 10 Injuries with Highest Team Performance Drop Index** | Color-coded severity gradient, hover details with days lost, sorted dynamically by points drop. |
| **2** | **Multi-Trace Line Timeline** | **Individual Player Performance Timeline Across Phases** | Interactive player dropdown, pre-injury baseline vs post-recovery return, highlighted absence duration rectangle. |
| **3** | **Spatiotemporal Heatmap** | **Monthly Injury Frequency Across Clubs & Calendar Months** | Magma density scale, calendar month ordering, reveals winter fixture congestion spikes (Nov–Jan). |
| **4** | **Scatter Plot with OLS Trendline** | **Player Age vs. Performance Drop Index & Recovery Days** | Positional color coding, bubble size scaled to recovery days, OLS linear regression line. |
| **5** | **Ranked Leaderboard Table** | **Comeback Players Ranked by Rating Improvement** | Dynamic sort by $\Delta$ Rating, color-graded resilience metrics, trajectory classification badges. |
| **6** | **Grouped Outcome Bar Chart** | **Team Win/Draw/Loss Distribution Across Phases** | Comparative breakdown of match outcomes with player active vs absent. |

---

## 🎮 Tactical Squad Simulator (Decision Support Tool)

Technical Directors can select a club and player to run a **What-If Injury Simulation**:
- Projects expected team points forfeited over a user-selected absence window (1–15 matches).
- Computes baseline vs depressed PPG.
- Recommends tactical adjustments (formation shifts, high-speed running load reductions).

