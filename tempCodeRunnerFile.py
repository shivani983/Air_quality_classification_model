ef predict(data, model):
#     # making predictions using the loaded models
#     if model == "svc_binary":
#         return svc_binary.predict(data)[0]
#     elif model == "svc_multi":
#         return svc_multi.predict(data)[0]
#     elif model == "logistic_binary":
#         return logistic_binary.predict(data)[0]
#     elif model == "logistic_ovr":
#         return logistic_ovr.predict(data)[0]
#     else:
#         return logistic_multi.predict(data)[0]
        
# def main():
#     st.write("Air Quality Prediction")


#     # Model selection
#     model = st.selectbox("Select a model", ["svc_binary", "svc_multi", "logistic_binary", "logistic_ovr", "logistic_multi"])
    
#     # Feature inputs
#     st.subheader("Enter Feature Values")
#     temperature = st.number_input("Temperature", min_value=0.0, max_value=100.0, value=25.0)
#     humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=50.0)
#     pm2_5 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=30.0)
#     pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=40.0)
#     no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, value=20.0)
#     so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, value=10.0)
#     co = st.number_input("CO", min_value=0.0, max_value=10.0, value=0.5)
#     proximity_to_industry = st.number_input("Proximity to Industrial Areas", min_value=0.0, max_value=10.0, value=5.0)
#     population_density = st.number_input("Population Density", min_value=0, max_value=1000000, value=50000)
    
#     user_data = np.array([[temperature, humidity, pm2_5, pm10, no2, so2, co, proximity_to_industry, population_density]])
    
#     # Load models
    
    
#     if st.button("Predict Air Quality"):
#         prediction = predict(user_data, model)
#         st.write(f"Predicted Air Quality: {prediction}")

# if __name__ == "__main__":
#     main()





         

