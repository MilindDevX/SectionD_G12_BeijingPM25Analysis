# SectionD_G12_BeijingPM25Analysis

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.
> **Submission Date:** April 29, 2026 | **Faculty Mentor:** Archit Raj

---

## Before You Start

1. Rename the repository using the format `SectionName_TeamID_ProjectName`.
2. Fill in the project details and team table below.
3. Add the raw dataset to `data/raw/`.
4. Complete the notebooks in order from `01` to `05`.
5. Publish the final dashboard and add the public link in `tableau/dashboard_links.md`.
6. Export the final report and presentation as PDFs into `reports/`.

### Quick Start

If you are working locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:

- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | SectionD_G12_BeijingPM25Analysis |
| **Sector** | Environmental Analytics / Public Health |
| **Team ID** | DVA - D - G12 |
| **Section** | Section D |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 29, 2026 |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Milind Bansal | MilindDevX |
| Data Lead | Milind Bansal | MilindDevX |
| ETL Lead | Milind Bansal | MilindDevX |
| Analysis Lead | Vishuti Jamwal | vishuti-jamwal |
| Visualization Lead | Hrishabh Prajapati | hrishu802 |
| Strategy Lead | Praveen Nitharwal | prav1104 |
| PPT and Quality Lead | Om Yadav | yadavom7345 |
| Report Lead | Samay Samrat | samay-hash |

---

## Business Problem

Fine particulate matter (PM2.5) represents the single greatest environmental health risk in urban China. During 2010–2014, Beijing's air quality remained chronically hazardous without a structured, data-backed decision framework for pollution alerts. Beijing's PM2.5 frequently exceeded the "Very Unhealthy" threshold (250 µg/m³), contributing significantly to cardiovascular and respiratory mortality in China. Without a data-backed alert framework, responses remain reactive and ineffective. This capstone develops a predictive analytics platform to translate meteorological and temporal patterns into operational public health guidance.

**Core Business Question**

> Which meteorological conditions and temporal patterns best predict hazardous PM2.5 levels in Beijing, and how can these be operationalised into a decision-support framework?

**Decision Supported**

> Trigger threshold-based public health alerts and advisories based on predicted high-risk PM2.5 conditions.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | UCI Machine Learning Repository (Liang et al., 2015) |
| **Direct Access Link** | https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data |
| **Row Count** | 43,824 |
| **Column Count** | 13 |
| **Time Period Covered** | 1 Jan 2010 – 31 Dec 2014 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| pm2.5 | PM2.5 concentration (µg/m³) | Target variable / KPI |
| DEWP | Dew point (°C) | Predictor / segmentation |
| TEMP | Temperature (°C) | Predictor / segmentation |
| cbwd | Combined wind direction (NW, NE, SE, cv) | Segmentation / filters |
| Iws | Cumulated wind speed (m/s) | Predictor / KPI |
| Ir / Is | Cumulated rain/snow hours | Precipitation flag / segmentation |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| Annual Mean PM2.5 | Average PM2.5 concentration across all hours in a year; primary compliance metric | Mean of all pm2.5 values in the target year |
| Hazardous Rate | Proportion of days with average PM2.5 exceeding 150 µg/m³ (moderate hazard threshold) | Count(days with avg PM2.5 > 150) / 365 |
| WHO Ratio | Annual mean PM2.5 relative to WHO guideline of 15 µg/m³; indicates breach magnitude | Annual Mean PM2.5 / 15 |
| AQI Distribution | Hourly distribution across AQI categories (Good, Moderate, Unhealthy, Very Unhealthy) | Count(hours in category) / total hours × 100% |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | https://public.tableau.com/app/profile/milind.bansal5979/viz/DVA2-Capstone/RiskSeverityOverview?publish=yes |
| **Executive View** | High-level KPI summary: Annual Mean PM2.5, WHO breach ratio (6–7×), hazardous days indicator, and AQI distribution overview |
| **Operational View** | Hour-vs-month heatmap showing temporal PM2.5 patterns, wind direction analysis by pollution level, seasonal breakdowns by KPI |
| **Main Filters** | Year, month, hour, AQI category, season, wind direction (cbwd) |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/README.md`](tableau/README.md).

---

## Key Insights

1. **WHO Guideline Breach Severity**: Beijing's annual mean PM2.5 exceeds the WHO guideline of 15 µg/m³ by 6–7 fold, indicating severe and chronic exposure across the population.

2. **No Improvement Trend (2010–2014)**: Despite regulatory efforts, air quality showed no statistically significant improvement over the 5-year study period, suggesting the need for more aggressive interventions.

3. **Hazardous Hours Prevalence**: Approximately 21% of all hours (roughly 1 in 5 days) recorded average PM2.5 concentrations in the hazardous range (>150 µg/m³).

4. **Winter Peak Pollution**: December through February exhibit 2–3× higher pollution levels compared to summer, driven by increased heating demand and stagnant meteorological conditions.

5. **Diurnal (Daily) Pattern**: Late-night and early-morning hours (8 PM–8 AM) show consistent PM2.5 spikes due to boundary layer collapse and reduced vertical mixing.

6. **Calm Wind Acceleration**: Calm wind conditions (cbwd='cv') show the highest average PM2.5 concentrations; wind speed emerges as the strongest single predictor of pollution levels.

7. **Northwest Wind Mitigation**: Northwest (NW) wind conditions are associated with the lowest PM2.5 concentrations, providing a "clean window" for high-emission activities.

8. **Precipitation Non-Impact**: Neither rainfall nor snowfall show statistically significant causal relationships with PM2.5 reduction; snow is a seasonal proxy rather than a direct driver.

9. **Wind Speed as Primary Predictor**: Cumulated wind speed (Iws) is the single most predictive meteorological variable; a 1 m/s increase correlates with measurable PM2.5 reduction.

10. **Summer Baseline Low**: Summer months (Jun–Aug) consistently show the lowest pollution levels (30–50 µg/m³), enabling seasonal benchmarking and improvement target-setting.

11. **Multi-Hour Lag Effects**: Temperature and dew point show lagged relationships with PM2.5 (4–12 hour delays), indicating atmospheric transport and mixing delays.

12. **AQI Category Skew**: Over 40% of hours fall into the "Unhealthy" or "Very Unhealthy" categories, with evening rush hour exacerbating peaks.

---

## Recommendations

_Provide 3-5 specific, actionable business recommendations, each linked directly to an insight above._

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Winter Peak Pollution (Insight 4) | Implement winter-priority emission reduction targeting coal heating infrastructure (Dec–Feb). Coordinate with district heating authorities to enforce scrubber upgrades and fuel switching. | 10–15% reduction in peak exposure during winter months; ~500,000 population benefiting from reduced respiratory hospitalizations. |
| 2 | Northwest Wind Mitigation (Insight 7) | Establish a "Clean Window" alert framework that triggers high-emission construction and industrial activities when NW winds exceed 21 m/s. Pre-position alerts 24–48 hours in advance using wind forecasts. | Improved advisory precision and operational timing; reduced acute pollution episodes during high-wind periods. |
| 3 | Calm Wind Emergency Protocols (Insight 6) | Deploy emergency industrial emission caps (cbwd='cv' conditions). Establish a "Red Alert" protocol limiting coal-fired power plant output and non-essential manufacturing when calm winds forecast. | Reduction of acute spikes (300+ µg/m³) by 20–30%; faster response to stagnant conditions. |
| 4 | Diurnal Monitoring Shift (Insight 5) | Migrate from daily AQI averaging to hourly-granular monitoring for health advisories, particularly capturing 8 PM–8 AM spikes. Issue rolling 4-hour pollution forecasts for evening commute planning. | Earlier warning for vulnerable populations; improved daily activity planning for asthmatics and elderly. |
| 5 | Wind Speed as Operational Lever (Insight 9) | Prioritize wind speed forecasting in the decision-support model. Use ensemble wind forecasts (24–72 hour lead time) to pre-position public health guidance and emission-reduction protocols. | Shift from reactive 6-hour advisories to proactive 48+ hour planning; 30–40% improvement in advisory adherence. |

---

## Repository Structure

```text
SectionD_G12_BeijingPM25Analysis/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- README.md
|   `-- screenshots/
|
|-- reports/
|   |-- Plots/
|   |-- report_dva.pdf
|   `-- ppt_dva.pdf
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-focused-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and optionally `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
| SQL | Optional | Initial data extraction only, if documented |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Contribution Matrix

| Name        | Data Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
|-------------|---------------|----------------|----------------|----------------------|-------------------|----------------|------------|
| Milind B.   | Owner         | Owner          | Support        | —                    | Support           | Support        | —          |
| Hrishabh    | —             | —              | Support        | Support              | Owner             | —              | —          |
| Om          | —             | Support        | —              | —                    | —                 | Owner          | Owner      |
| Vishuti J.  | —             | —              | Owner          | Owner                | —                 | Support        | —          |
| Samay S     | —             | —              | —              | Support              | —                 | Owner          | Support    |
| Praveen N.  | Support       | —              | Support        | Support              | Owner             | —              | —          |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Milind Bansal

**Date:** 28/4/2026

---

## Academic Integrity

All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
