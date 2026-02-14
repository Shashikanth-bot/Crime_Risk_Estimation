import pandas as pd
import random

# Load CSV
crime_df = pd.read_csv("city_crime_rates.csv")

# Normalize column names
crime_df.columns = crime_df.columns.str.strip().str.lower().str.replace(" ", "")

# Auto-detect required columns
city_col = None
crime_col = None
rate_col = None

for col in crime_df.columns:
    if col.startswith("city"):
        city_col = col
    if "crime" in col and "type" in col:
        crime_col = col
    if "lakh" in col:
        rate_col = col

if not all([city_col, crime_col, rate_col]):
    raise Exception("Required columns not found in city_crime_rates.csv")

# 🔧 FORCE numeric conversion for crime rate
crime_df[rate_col] = pd.to_numeric(crime_df[rate_col], errors="coerce")

# Drop rows where conversion failed
crime_df = crime_df.dropna(subset=[rate_col])

rows = []

for _, row in crime_df.iterrows():
    for _ in range(20):  # samples per city-crime
        rows.append({
            "city": row[city_col],
            "crime": row[crime_col],
            "fatal": random.choice([0, 1]),
            "pending": random.choice([0, 1]),
            "gender": random.choice(["male", "female"]),
            "base_rate": float(row[rate_col])
        })

ml_df = pd.DataFrame(rows)

# Normalize base rate safely
max_rate = ml_df["base_rate"].max()
ml_df["base_rate_norm"] = ml_df["base_rate"] / max_rate

# Ethical exposure score (derived, explainable)
ml_df["exposure_score"] = (
    ml_df["base_rate_norm"] * 100
    * (1 + ml_df["fatal"] * 0.25)
    * (1 + ml_df["pending"] * 0.10)
    * (1 + (ml_df["gender"] == "male") * 0.05)
)

ml_df["exposure_score"] = ml_df["exposure_score"].clip(0, 100)

# Save training data
ml_df.to_csv("ml_training_data.csv", index=False)

print("ML training data generated successfully:", len(ml_df), "rows")
