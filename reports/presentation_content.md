# Beijing PM2.5 Analysis - Presentation Content

Use this document to draft the final presentation slides based on the analysis of the Beijing PM2.5 dataset.

---

## Slide 1 - Title

- **Project Title:** Beijing PM2.5 Analysis & Alert Optimization
- **Sector:** Public Health & Environmental Monitoring
- **Team ID:** [Insert Team ID e.g., DVA-B1-T3]
- **Team Members:** [Insert Team Members]
- **Faculty Mentor:** [Insert Mentor Name]

---

## Slide 2 - Context and Problem Statement

- **Sector Context:** Air pollution is a severe public health hazard in rapidly developing urban centers, leading to significant respiratory illnesses and economic impact.
- **Stakeholder:** City Environmental Protection Bureau / Public Health Officials.
- **Core Problem Statement:** At what hours, months, and weather conditions does PM2.5 exceed unsafe levels most consistently, so authorities can decide when to trigger targeted pollution alerts and mitigation actions?
- **Decision Supported:** This analysis will enable stakeholders to decide when to issue high-risk air-quality alerts and deploy targeted interventions (e.g., traffic restrictions, construction controls, and public health advisories) based on the time periods and weather conditions most associated with unsafe PM2.5 levels.

---

## Slide 3 - Data Engineering

- **Source:** UCI Machine Learning Repository (US Embassy, Beijing).
- **Size and Coverage:** 43,824 rows across 5 years (Jan 1, 2010 – Dec 31, 2014) representing hourly granularity.
- **Major Cleaning Steps:** 
  - Standardized datetime format for time-series compatibility.
  - Addressed missing PM2.5 values (~4.7%) by applying forward-fill (and backward-fill for leading nulls) to preserve timeline integrity without aggressive data dropping.
- **Data Dictionary Summary:** Key variables include `pm2_5_cleaned` (target variable), `temperature`, `dew_point`, `pressure`, `wind_direction`, and `wind_speed`.

---

## Slide 4 - KPI Framework

- **Target KPI 1: Percentage of Hours with PM2.5 Above 150 µg/m³**
  - *Definition:* The frequency of extreme health risks in the recorded data.
  - *Why it matters:* Measures how often conditions become hazardous, guiding the necessity and volume of emergency alerts.
- **Target KPI 2: Average PM2.5 Concentration (µg/m³)**
  - *Definition:* The absolute baseline level of PM2.5 in the air.
  - *Why it matters:* Acts as the primary metric for tracking overall air quality trends against the WHO safe limit of 15 µg/m³.
- **Target KPI 3: Worst Month**
  - *Definition:* The calendar month exhibiting the highest frequency of hazardous PM2.5 levels (e.g., Oct with 31.3% of hours).
  - *Why it matters:* Essential for strategic planning, allowing authorities to pre-allocate resources and schedule interventions before peak pollution seasons.
- **Target KPI 4: Peak Hour**
  - *Definition:* The specific hour of the day recording the highest average PM2.5 concentration (e.g., 1 AM averaging 112.4 µg/m³).
  - *Why it matters:* Crucial for daily operational planning, such as adjusting outdoor work schedules and broadcasting targeted health advisories to vulnerable populations.
- **Expected Insight:** We expect to find that PM2.5 levels are significantly higher during winter months and low-wind conditions, and lower during periods with stronger wind or rainfall, indicating a clear relationship between weather patterns and pollution intensity.

---

## Slide 5 - Key EDA Insights

- **Consistently High Baseline:** The mean PM2.5 is 97.8 µg/m³ (over 6x the WHO limit), showing hazardous conditions are a recurring pattern.
- **Night-Time Spikes:** Pollution peaks between midnight and 2 AM (112.4 µg/m³) and reaches its lowest around 3–4 PM due to atmospheric mixing and temperature inversions.
- **Wind Direction Matters:** Northwesterly winds clear pollution (avg 69.8 µg/m³), while calm/variable conditions allow it to accumulate (avg 124.5 µg/m³).
- **Winter Peaks:** February and October have the highest PM2.5, strongly associated with increased coal heating and lower atmospheric dispersion.
- **Alarming AQI Category:** Over half of all recorded hours (58.7%) fall into the "Unhealthy", "Very Unhealthy", or "Hazardous" categories.

---

## Slide 6 - Advanced Analysis

- **Statistical Method:** Non-parametric tests were used (Shapiro-Wilk test confirmed PM2.5 is non-normally distributed). Applied Mann-Whitney U, Kruskal-Wallis, and Spearman correlations.
- **Wind Speed Effect (Spearman Correlation):** Confirmed as the strongest negative predictor of PM2.5 (r = -0.35, p < 0.001); higher winds are consistently associated with lower pollution.
- **Seasonal Significance (Kruskal-Wallis):** Statistically significant differences across seasons (p < 0.001). Winter is confirmed as the highest pollution season, making it a reliable alert variable.
- **Rain & Snow Signals (Mann-Whitney U):** Rain has no statistically significant independent effect on PM2.5 (p = 0.63). Snow is correlated with higher PM2.5, but acts as a co-occurring winter signal rather than a direct cause.

---

## Slide 7 - Tableau Dashboard Walkthrough

- **DASHBOARD URL**
  - https://public.tableau.com/app/profile/milind.bansal5979/viz/DVA2-Capstone/RiskSeverityOverview?publish=yes

- **1. PAGE 1 — RISK & SEVERITY OVERVIEW**
  - **Subtitle:** How bad is it? AQI classification & hazardous day tracking
  - **KPIs:** Overall avg PM2.5 (97.8 µg/m³) · Avg hazardous days / year (71.8 days) · Very Unhealthy + Hazardous (21.2%) · Peak PM2.5 recorded (994 µg/m³)
  - **Charts:** AQI category breakdown · Hazardous days per year · Annual Trend
  - **Filters:** AQI Category · Year

- **2. PAGE 2 — TEMPORAL PATTERNS**
  - **Subtitle:** When does pollution peak?
  - **KPIs:** Mean PM2.5 (97.8 µg/m³) · % Hours Above 150 (21.2%) · Worst Month (Oct - 31.3% of hours) · Peak Hour (1 AM - avg 112.4 µg/m³)
  - **Charts:** % Hours Above 150 by Month · Hourly Average PM2.5 · Hour x Month Heatmap
  - **Filters:** Hour · Year · Month

- **3. PAGE 3 — WEATHER & CONDITIONS**
  - **Subtitle:** What drives pollution? Wind, season & precipitation
  - **KPIs:** Calm vs NW wind gap (54.7 µg/m³) · Wind Speed Spearman r (-0.35) · Winter vs Spring gap (21.7 µg/m³) · Rain Effect p-value (0.63)
  - **Charts:** PM2.5 by Wind Speed Range · PM2.5 by Wind Direction · PM2.5 by Season · Precipitation
  - **Filters:** Precipitation Type · Season · Wind Direction · Wind Speed

---

## Slide 8 - Top Insights

1. **Wind Speed is the Best Cleanser:** Strong winds, particularly from the Northwest, disperse pollutants, whereas calm conditions allow rapid hazardous accumulation.
2. **Pollution is Highly Seasonal & Diurnal:** It spikes predictably in winter months and late-night hours due to coal heating and reduced atmospheric turbulence.
3. **Precipitation is a False Trigger:** Rainfall does not significantly clear PM2.5 pollution; tying alerts to rain forecasts is ineffective.
4. **No Significant Improvement:** Across the 5-year study window, annual means fluctuated but showed no consistent downward trend toward WHO guidelines.

---

## Slide 9 - Recommendations

- **Recommendation 1: Wind-Based Warning Systems**
  - Implement automated public health warnings when sustained calm/variable winds are forecasted during winter, as this precedes hazardous accumulation.
- **Recommendation 2: Targeted Winter Interventions**
  - Allocate peak resources (e.g., mask distribution, vulnerable population warnings) explicitly between October and February.
- **Recommendation 3: Restructure Night Shifts**
  - For outdoor workers, avoid scheduling heavy outdoor activity between midnight and 3 AM when pollution hits its diurnal peak.

---

## Slide 10 - Impact

- **Expected Outcome:** 
  - Reduced emergency room visits due to respiratory issues by enabling citizens to take pre-emptive protective measures before pollution spikes.
  - Better allocation of municipal resources based on highly predictable seasonal/diurnal timing.
- **Priority and Feasibility:** 
  - High Priority, High Feasibility. Meteorological data (wind speed/direction and season) is already tracked continuously, making an alert API easy to integrate.

---

## Slide 11 - Limitations

- **Single Monitoring Station:** Data represents only central Beijing (US Embassy sensor) and cannot be accurately generalized to suburban or rural areas.
- **Confounding Variables:** The dataset lacks economic or emission-source data (e.g., industrial output, traffic volume) which limits the ability to isolate exact causes of pollution spikes.
- **Cumulative Meteorological Readings:** Rain and snow are recorded as cumulative hours, not instantaneous intensity, making complex weather modeling challenging.

---

## Slide 12 - Next Steps

- **Future Extensions:** 
  - Incorporate multi-station data to build a spatial heatmap of pollution across different Beijing districts.
  - Add proxy data for emission sources (e.g., traffic density, coal plant outputs) to perform root-cause analysis on the pollution itself.
- **Closing Summary:** 
  - Beijing's PM2.5 problem remains persistently severe, but its strong correlations with wind patterns, seasons, and time of day offer a clear pathway to a highly predictive, data-driven early warning system.
