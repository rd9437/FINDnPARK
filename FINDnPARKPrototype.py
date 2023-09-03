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
        
        if probability > 0.8:
            result_sentence = "This is a good hour to find a parking spot."
        elif probability > 0.5:
            result_sentence = "This hour might have moderate occupancy."
        else:
            result_sentence = "This is not a good hour to find a parking spot."
        
        prediction = f"Chances of getting a parking spot at {input_hour}: {probability:.2%}. {result_sentence}"
        return prediction
    else:
        return "Invalid input. Please provide a valid day and time."

import streamlit as st

import streamlit as st

# Streamlit UI
st.title("FINDnPARK 1.0")

# Define a CSS style for the app with the background image URL
app_style = f"""
<style>
body {{
    background-image: url('https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-LWamoztjI1H7rn5R3L26A.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""

# Set the CSS style for the app
st.markdown(app_style, unsafe_allow_html=True)

input_day = st.text_input("Enter a day (e.g., Monday):")
input_hour = st.text_input("Enter the hour (e.g., 8AM - 8PM):")

if st.button("Predict"):
    prediction = predict_parking_probability(input_day, input_hour)
    st.write(prediction)

