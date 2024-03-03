import streamlit as st
import pandas as pd

# Load CSV data into a DataFrame
data = pd.read_csv('parkingdataset.csv')

# Prediction function
def predict_parking_slots(input_day, input_hour):
    if input_hour in data.columns and input_day in data['Day'].unique():
        total_slots = data['Total Slots'][data['Day'] == input_day].sum()
        occupied = data[input_hour][data['Day'] == input_day].sum()
        
        if pd.isnull(total_slots) or pd.isnull(occupied):
            return f"At {input_hour}: No data available to calculate slots."
        
        probability = 1 - (occupied / total_slots)
      
        expected_available_slots = int(probability * 218)
        
        return f"Expected available parking slots: {expected_available_slots} slots"
    else:
        return "Invalid input. Please provide a valid day and time."

# Streamlit UI
st.title("FINDnPARK 1.0")

input_day = st.text_input("Enter a day (e.g., Monday):")
input_hour = st.text_input("Enter the hour (e.g., 8AM - 8PM):")

if st.button("Find Space"):
    prediction = predict_parking_slots(input_day, input_hour)
    st.write(prediction)

# Disclaimer message
st.write("\n")
st.write("### Disclaimer")
st.write("This application is part of an ongoing project aimed at analyzing parking space availability using a dataset. Please note that this application is still under construction, and its predictions may not be accurate or reliable. Users are advised not to rely solely on the information provided by this application for their parking decisions. Thank you for your understanding.")
