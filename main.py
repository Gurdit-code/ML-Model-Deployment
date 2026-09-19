from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices in India",
    version="1.0.0")


try:
    model = joblib.load("model/house_price_model.pkl")
    logger.info("Model loaded successfully")
except Exception as e:
    model = None
    logger.error(f"Could not load model: {e}")


class HouseInput(BaseModel):
    City: str = Field(..., min_length=2)
    Location: str = Field(..., min_length=2)
    BHK: int = Field(..., gt=0)
    Area_sqft: float = Field(..., gt=0)
    Bathrooms: int = Field(..., gt=0)
    Age: int = Field(..., ge=0)


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running",
        "docs": "/docs",
        "health": "/health"}


@app.get("/health")
def health():
    if model is None:
        return {
            "status": "unhealthy",
            "model": "not loaded" }

    return {"status": "healthy", "model": "loaded"}


@app.post("/predict")
def predict(data: HouseInput):

    if model is None:
        raise HTTPException(status_code=503, detail="Model is not available")

    try:
        input_data = pd.DataFrame([{
            "City": data.City,
            "Location": data.Location,
            "BHK": data.BHK,
            "Area_sqft": data.Area_sqft,
            "Bathrooms": data.Bathrooms,
            "Age": data.Age
        }])

        prediction = model.predict(input_data)[0]
        return {
            "predicted_price_lakh": round(float(prediction), 2)
            }

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")