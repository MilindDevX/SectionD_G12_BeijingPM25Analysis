"""ETL pipeline for Beijing PM2.5 Analysis — NST DVA Capstone 2.

This script contains the full cleaning pipeline for the Beijing PM2.5 dataset
(PRSA_data_2010.1.1-2014.12.31.csv). It extends the starter basic_clean()
function with a dataset-specific clean_beijing_pm25() function.

Can be run directly from the command line or imported into notebooks 01 and 02.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


# ── Generic helpers (from starter template) ───────────────────────────────────

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply safe default cleaning steps — dedup, normalize columns, strip strings."""
    result = normalize_columns(df)
    result = result.drop_duplicates().reset_index(drop=True)
    for column in result.select_dtypes(include="object").columns:
        result[column] = result[column].astype("string").str.strip()
    return result


# ── Beijing PM2.5 specific helpers ────────────────────────────────────────────

def get_season(month: int) -> str:
    """Map a month number to a meteorological season."""
    if month in [12, 1, 2]:   return "Winter"
    elif month in [3, 4, 5]:  return "Spring"
    elif month in [6, 7, 8]:  return "Summer"
    else:                      return "Autumn"


def get_aqi_category(val: float) -> str:
    """Map a PM2.5 concentration (µg/m³) to a US EPA AQI category."""
    if val <= 12:              return "Good"
    elif val <= 35.4:          return "Moderate"
    elif val <= 55.4:          return "Unhealthy for Sensitive Groups"
    elif val <= 150.4:         return "Unhealthy"
    elif val <= 250.4:         return "Very Unhealthy"
    else:                      return "Hazardous"


# ── Main cleaning pipeline ─────────────────────────────────────────────────────

def clean_beijing_pm25(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline for the Beijing PM2.5 dataset.

    Transformations applied:
    1. Drop the 'No' row-index column (no analytical value).
    2. Create a single 'datetime' column from year/month/day/hour.
    3. Rename all columns to snake_case.
    4. Impute missing pm2_5 values into a new 'pm2_5_cleaned' column
       using forward-fill then backward-fill.
    5. Derive 'season' from month.
    6. Derive 'aqi_category' from pm2_5_cleaned using US EPA breakpoints.
    7. Reorder and sort by datetime.

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataframe loaded directly from the CSV.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with 16 columns, 43,824 rows.
    """

    df = df.copy()

    # 1. Drop row index
    df = df.drop(columns=["No"])

    # 2. Create datetime column
    df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])

    # 3. Rename columns
    df = df.rename(columns={
        "pm2.5":  "pm2_5",
        "DEWP":   "dew_point",
        "TEMP":   "temperature",
        "PRES":   "pressure",
        "cbwd":   "wind_direction",
        "Iws":    "wind_speed",
        "Is":     "hours_snow",
        "Ir":     "hours_rain",
    })

    # 4. Impute missing pm2_5
    df["pm2_5_cleaned"] = df["pm2_5"].ffill().bfill()

    # 5. Derived: season
    df["season"] = df["month"].apply(get_season)

    # 6. Derived: AQI category
    df["aqi_category"] = df["pm2_5_cleaned"].apply(get_aqi_category)

    # 7. Reorder columns and sort
    df = df[[
        "datetime", "year", "month", "day", "hour",
        "pm2_5", "pm2_5_cleaned", "aqi_category", "season",
        "dew_point", "temperature", "pressure",
        "wind_direction", "wind_speed", "hours_snow", "hours_rain",
    ]]
    df = df.sort_values("datetime").reset_index(drop=True)

    return df


# ── I/O helpers ────────────────────────────────────────────────────────────────

def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read the raw CSV and return a cleaned dataframe."""
    df = pd.read_csv(input_path)
    return clean_beijing_pm25(df)


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write cleaned dataframe to disk, creating parent folders if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# ── CLI entrypoint ─────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Beijing PM2.5 ETL pipeline.")
    parser.add_argument("--input",  required=True, type=Path, help="Path to raw CSV in data/raw/.")
    parser.add_argument("--output", required=True, type=Path, help="Path for cleaned CSV in data/processed/.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)
    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(cleaned_df)} | Columns: {len(cleaned_df.columns)}")


if __name__ == "__main__":
    main()
