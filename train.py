import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score


# Load data
df = pd.read_csv("data/India_house_prices.csv")

print("Dataset loaded successfully")
print(df.head())
print("Dataset shape:", df.shape)

X = df.drop("Price_Lakh", axis=1)
y = df["Price_Lakh"]


categorical_features = ["City", "Location"]

numerical_features = [
    "BHK",
    "Area_sqft",
    "Bathrooms",
    "Age" ]


# Preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ("cat",OneHotEncoder(handle_unknown="ignore"),
            categorical_features),
        ("num",StandardScaler(),numerical_features)
    ])

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
        ])


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
pipeline.fit(X_train, y_train)

print("Model trained successfully")
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test,predictions)

print(f"Mean Absolute Error: {mae:.2f} lakh")
print(f"R2 Score: {r2:.2f}")

joblib.dump(pipeline,"model/house_price_model.pkl")
print("Model saved successfully")

