import streamlit as st
import pandas as pd

# Load CSV data into a DataFrame
data = pd.read_csv('parkingdataset.csv')

# Prediction function
def predict_parking_percentage(input_day, input_hour):
    if input_hour in data.columns and input_day in data['Day'].unique():
        total_slots = data['Total Slots'][data['Day'] == input_day].sum()
        occupied = data[input_hour][data['Day'] == input_day].sum()
        
        if pd.isnull(total_slots) or pd.isnull(occupied):
            return f"At {input_hour}: No data available to calculate percentage."
        
        probability = 1 - (occupied / total_slots)
        
        # Calculate expected available parking slots as a percentage of the total slots (218) and round to the nearest integer
        expected_available_percentage = int(probability * 218)
        
        return f"Expected available parking slots as a percentage of the total slots (218): {expected_available_percentage}%"
    else:
        return "Invalid input. Please provide a valid day and time."

# Streamlit UI
st.title("FINDnPARK 1.0")

input_day = st.text_input("Enter a day (e.g., Monday):")
input_hour = st.text_input("Enter the hour (e.g., 8AM - 8PM):")

if st.button("Predict"):
    prediction = predict_parking_percentage(input_day, input_hour)
    st.write(prediction)
