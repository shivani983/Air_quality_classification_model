import pandas as pd
import numpy as np
import joblib
import streamlit as st

def load_models():
    """Load all trained models from pickle files."""
    return {
        "svc_binary": joblib.load("svc_binary.pkl"),
        "svc_multi": joblib.load("svc_multi.pkl"),
        "logistic_binary": joblib.load("logistic_binary.pkl"),
        "logistic_ovr": joblib.load("logistic_ovr.pkl"),
        "logistic_multi": joblib.load("logistic_multi.pkl")
    }

def predict(data, model, models):
    """Make predictions using the selected model."""
    return models[model].predict(data)[0]

def main():
    st.title("Air Quality Prediction")
    
    # Load models
    models = load_models()
    
    # Model selection
    model = st.selectbox("Select a model", list(models.keys()))
    
    # Feature inputs
    st.subheader("Enter Feature Values")
    temperature = st.number_input("Temperature", min_value=0.0, max_value=100.0, value=25.0)
    humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=50.0)
    pm2_5 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=30.0)
    pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=40.0)
    no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, value=20.0)
    so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, value=10.0)
    co = st.number_input("CO", min_value=0.0, max_value=10.0, value=0.5)
    proximity_to_industry = st.number_input("Proximity to Industrial Areas", min_value=0.0, max_value=10.0, value=5.0)
    population_density = st.number_input("Population Density", min_value=0, max_value=1000000, value=50000)
    
    user_data = np.array([[temperature, humidity, pm2_5, pm10, no2, so2, co, proximity_to_industry, population_density]])
    
    if st.button("Predict Air Quality"):
        prediction = predict(user_data, model, models)
        st.write(f"Predicted Air Quality: {prediction}")

        # Categorizing the prediction
        if prediction == 0:
            air_quality = "Good"
        elif prediction == 1:
            air_quality = "Moderate"
        else:
            air_quality = "Bad"

        # Display the categorized result
        st.success(f"Air Quality is: {air_quality}")


if __name__ == "__main__":
    main()
