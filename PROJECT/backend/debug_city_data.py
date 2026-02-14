import pandas as pd

df = pd.read_csv("city_crime_rates.csv")

print("RAW COLUMNS:")
print(df.columns.tolist())

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATA TYPES:")
print(df.dtypes)
