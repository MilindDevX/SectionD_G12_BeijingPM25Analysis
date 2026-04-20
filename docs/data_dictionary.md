# Data Dictionary — Beijing PM2.5 Analysis

## Dataset Summary

| Item | Details |
|---|---|
| Dataset Name | Beijing PM2.5 Hourly Air Quality Data |
| Source | UCI Machine Learning Repository |
| Raw File Name | `PRSA_data_2010.1.1-2014.12.31.csv` |
| Rows | 43,824 |
| Columns | 13 (raw) → 14 (cleaned) |
| Granularity | One row per hour, single monitoring station (US Embassy, Beijing) |
| Time Period | 1 Jan 2010 — 31 Dec 2014 |

---

## Column Definitions

### Raw Columns

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `No` | int | Row index from the original source file. Carries no analytical meaning. | 1 | — | Dropped during ETL. |
| `year` | int | Year of the observation. | 2013 | EDA, Tableau filter | Kept as-is. Also used to build `datetime`. |
| `month` | int | Month of the observation (1–12). | 7 | EDA, Tableau filter | Kept as-is. Also used to build `datetime`. |
| `day` | int | Day of the month (1–31). | 15 | EDA | Kept as-is. Also used to build `datetime`. |
| `hour` | int | Hour of the day in 24h format (0–23). | 14 | EDA, trend analysis | Kept as-is. Also used to build `datetime`. |
| `pm2.5` | float | Hourly PM2.5 concentration in micrograms per cubic metre (µg/m³). Core target variable. | 129.0 | KPI, EDA, Tableau | Renamed to `pm2_5`. 2,067 nulls present — preserved in cleaned dataset as-is. |
| `DEWP` | int | Dew point temperature in degrees Celsius. Indicator of atmospheric humidity. | -21 | EDA, correlation analysis | Renamed to `dew_point`. No nulls. |
| `TEMP` | float | Ambient air temperature in degrees Celsius. | -11.0 | EDA, correlation analysis | Renamed to `temperature`. No nulls. |
| `PRES` | float | Atmospheric pressure in hPa. | 1021.0 | EDA, correlation analysis | Renamed to `pressure`. No nulls. |
| `cbwd` | string | Combined wind direction. One of four categories: `NW`, `NE`, `SE`, `cv` (calm/variable). | NW | EDA, Tableau filter | Renamed to `wind_direction`. No nulls. |
| `Iws` | float | Cumulative wind speed in metres per second (m/s). | 1.79 | EDA, correlation analysis | Renamed to `wind_speed`. No nulls. |
| `Is` | int | Cumulative number of hours of snow in the preceding hour. | 0 | EDA | Renamed to `hours_snow`. No nulls. |
| `Ir` | int | Cumulative number of hours of rain in the preceding hour. | 0 | EDA | Renamed to `hours_rain`. No nulls. |

---

### Cleaned / Processed Columns

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `datetime` | datetime | Single timestamp column merged from `year`, `month`, `day`, and `hour`. | 2013-07-15 14:00:00 | EDA, Tableau time axis | Derived during ETL using `pd.to_datetime()`. |
| `pm2_5_cleaned` | float | PM2.5 concentration with missing values filled. Nulls forward-filled using the previous hour's value; any leading nulls at the start of the series are backward-filled. | 129.0 | KPI, Tableau primary measure | Derived during ETL. Use this column for all analysis and dashboarding. |

---

## Derived Columns

| Derived Column | Logic | Purpose |
|---|---|---|
| `datetime` | `pd.to_datetime(df[['year', 'month', 'day', 'hour']])` | Enables time-series plotting and Tableau date filters without manual parsing. |
| `pm2_5_cleaned` | `df['pm2_5'].ffill().bfill()` | Provides a complete, null-free PM2.5 series suitable for trend analysis, aggregation, and Tableau visualizations. |

---

## Data Quality Notes

- **2,067 missing PM2.5 values (~4.7%)** — spread across all five years. Most concentrated in 2010 and 2011. Missing values in the raw `pm2_5` column are intentionally preserved. Use `pm2_5_cleaned` for analysis.
- **Wind direction value `cv`** — stands for calm/variable wind. It is not a compass direction. Treat it as a distinct category in Tableau filters and groupings.
- **PM2.5 values above 500 µg/m³** — 125 such rows exist (max: 994 µg/m³). These are extreme pollution events, not sensor errors. Do not remove them — they are analytically significant.
- **Single monitoring station** — all data comes from one station at the US Embassy in Beijing. Findings represent central Beijing only and should not be generalised to other parts of the city.
- **Cumulative wind/precipitation columns** (`wind_speed`, `hours_snow`, `hours_rain`) — these are cumulative within a weather event, not instantaneous readings. Keep this in mind when interpreting spikes.
