import streamlit as st
import pandas as pd

# Load CSV data into a DataFrame
data = pd.read_csv('parkingdataset.csv')

# Prediction function
def predict_parking_probability(input_day, input_hour):
    if input_hour in data.columns and input_day in data['Day'].unique():
        total_slots = data['Total Slots'][data['Day'] == input_day].sum()
        occupied = data[input_hour][data['Day'] == input_day].sum()
        
        if pd.isnull(total_slots) or pd.isnull(occupied):
            return f"At {input_hour}: No data available to calculate probability."
        
        probability = 1 - (occupied / total_slots)
        
        # Convert probability to a whole number percentage
        probability_percentage = round(probability * 100)
        
        if probability_percentage > 80:
            result_sentence = "This is a good hour to find a parking spot."
        elif probability_percentage > 50:
            result_sentence = "This hour might have moderate occupancy."
        else:
            result_sentence = "This is not a good hour to find a parking spot."
        
        prediction = f"Chances of getting a parking spot at {input_hour}: {probability_percentage}%. {result_sentence}"
        return prediction
    else:
        return "Invalid input. Please provide a valid day and time."

# Streamlit UI
st.title("FINDnPARK 1.0")

input_day = st.text_input("Enter a day (e.g., Monday):")
input_hour = st.text_input("Enter the hour (e.g., 8AM - 8PM):")

if st.button("Predict"):
    prediction = predict_parking_probability(input_day, input_hour)
    st.write(prediction)
