import streamlit as st
import pandas as pd
import json
import os

# Create a data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

user_data_file = os.path.join("data", "userDB.csv")

st.title("User Information Collection")

# User Information
st.subheader("User Details")
name = st.text_input("Name")
dob = st.date_input("Date of Birth")
gender = st.radio("Gender", ("Male", "Female", "Other"))
email = st.text_input("Email")
language = st.selectbox("Preferred Language", ("English", "Hindi", "Bengali", "Tamil"))

# JSON File Upload for Listening History
st.subheader("Upload Your Listening History (CSV)")
uploaded_file = st.file_uploader("Choose a JSON file", type=["csv"])
listening_history = None

if uploaded_file is not None:
    listening_history = json.load(uploaded_file)

# Customized "Style your Taste" Button
if st.button("Style your Taste"):
    # Create a user dictionary
    user_data = {
        "Name": name,
        "Date of Birth": dob,
        "Gender": gender,
        "Email": email,
        "Preferred Language": language,
        "Listening History": listening_history
    }

    # Create a user data DataFrame
    user_df = pd.DataFrame([user_data])

    # Save user data to a CSV file
    if not os.path.exists(user_data_file):
        user_df.to_csv(user_data_file, index=False)
    else:
        user_df.to_csv(user_data_file, mode="a", header=False, index=False)

    st.success("User data submitted successfully.")

# Display user data table
if os.path.exists(user_data_file):
    st.subheader("User Data")
    user_data_df = pd.read_csv(user_data_file)
    st.write(user_data_df)
