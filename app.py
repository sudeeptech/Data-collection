import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(page_title="Data Collection App", page_icon="📝", layout="centered")

# App Title
st.markdown("<h2 style='color:red; text-align:center;'>📝 Data Collection App</h2>", unsafe_allow_html=True)
st.write("Please enter your details below. The data will be securely stored in a CSV file.")

# User Inputs
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
feedback = st.text_area("Enter feedback")

# Folder to save data
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)
file_path = os.path.join(data_folder, "user_feedback.csv")

# Save Button
if st.button("Save Data"):
    if name and email and feedback:
        data = {"Name": [name], "Email": [email], "Feedback": [feedback]}
        df = pd.DataFrame(data)

        if os.path.exists(file_path):
            df.to_csv(file_path, mode="a", header=False, index=False)
        else:
            df.to_csv(file_path, index=False)

        st.success("✅ Data saved successfully!")
    else:
        st.warning("⚠️ Please fill all fields before saving.")

# Footer
st.markdown("<div style='text-align:center; color:red; margin-top:30px;'>Developed by Sudeep using Machine Learning</div>", unsafe_allow_html=True)
