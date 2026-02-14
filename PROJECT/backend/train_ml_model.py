import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load ML training data
df = pd.read_csv("ml_training_data.csv")

# Encode categorical columns
le_city = LabelEncoder()
le_crime = LabelEncoder()
le_gender = LabelEncoder()

df["city"] = le_city.fit_transform(df["city"])
df["crime"] = le_crime.fit_transform(df["crime"])
df["gender"] = le_gender.fit_transform(df["gender"])

# Features and target
X = df[["city", "crime", "fatal", "pending", "gender", "base_rate_norm"]]
y = df["exposure_score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, "exposure_ml_model.pkl")
joblib.dump(le_city, "le_city.pkl")
joblib.dump(le_crime, "le_crime.pkl")
joblib.dump(le_gender, "le_gender.pkl")

print("ML model trained and saved successfully")
