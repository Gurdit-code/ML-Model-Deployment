import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="House Price Prediction",page_icon="🏠",
    layout="centered")

API_URL = "http://127.0.0.1:8000/predict"

df = pd.read_csv("data/India_house_prices.csv")

st.title("🏠 House Price Prediction")
st.write("Enter the house details to estimate its price.")

cities = sorted(df["City"].unique())
city = st.selectbox("City", cities)

locations = sorted(df[df["City"] == city]["Location"].unique())
location = st.selectbox("Location",locations)

bhk = st.number_input("Number of BHK",min_value=1, max_value=10, value=2, step=1)
area_sqft = st.number_input("House Area (sq ft)", min_value=100.0,value=1100.0, step=50.0)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2, step=1)

age = st.number_input( "Property Age (years)", min_value=0, max_value=100, value=5, step=1)


if st.button("Predict House Price"):

    if not location.strip():
        st.warning("Please enter the house location.")

    else:
        data = {
            "City": city,
            "Location": location,
            "BHK": bhk,
            "Area_sqft": area_sqft,
            "Bathrooms": bathrooms,
            "Age": age  }
        
        try:
            response = requests.post(
                API_URL,
                json=data,
                timeout=10)

            if response.status_code == 200:
                result = response.json()
                predicted_price = result["predicted_price_lakh"]
                st.success("Prediction successful!")
                st.metric(label="Estimated House Price",
                    value=f"₹ {predicted_price:,.2f} Lakh")

            else:
                st.error(
                    f"API Error: {response.status_code}" )

                st.write(response.text)
        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to FastAPI. " 
                "Make sure the API is running on port 8000." )

        except requests.exceptions.Timeout:
            st.error("The API request timed out.")

        except Exception as e:

            st.error(
                f"Something went wrong: {e}")