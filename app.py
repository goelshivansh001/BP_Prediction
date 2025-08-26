import numpy as np
import streamlit as st
import pandas as pd
import joblib
import os
import sklearn as skt
import warnings
warnings.filterwarnings("ignore")

import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "bp_model.pkl")

grid = joblib.load(model_path)


# st.title("🩺 Blood Pressure Prediction App")
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 Blood Pressure Prediction App</h1>", unsafe_allow_html=True)
st.write("---")

# 📌 Basic Info Section
st.subheader("👤 Basic Information")
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age (years)", 1, 100, 25)
    height = st.slider("Height (m)", 1.3, 2.2, 1.7)

with col2:
    weight = st.slider("Weight (kg)", 25, 200, 70)
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

# Auto Calculate BMI
bmi = round(weight / (height ** 2), 2)
st.info(f"📏 Your BMI is **{bmi}**")

# 📌 Lifestyle & Health Section
st.subheader("🏥 Lifestyle & Health Factors")
col3, col4 = st.columns(2)

with col3:
    chol = st.selectbox("Cholesterol Level", ["Low", "Medium", "High"])
    smoke = st.radio("Do you smoke?", ["Yes", "No"], horizontal=True)

with col4:
    glucose = st.selectbox("Glucose Level", ["Low", "Medium", "High"])
    activity = st.radio("Physically Active?", ["Yes", "No"], horizontal=True)

# Extra question
cvd = st.radio("Any Cardiovascular Disease?", ["Yes", "No"], horizontal=True)

st.write("---")

# 🔹 Mapping categorical values
gender_map = {"Male": 0, "Female": 1}
chol_map = {"Low": 0, "Medium": 1, "High": 2}
smoke_map = {"Yes": 1, "No": 0}
glucose_map = {"Low": 0, "Medium": 1, "High": 2}
activity_map = {"Yes": 1, "No": 0}
cvd_map = {"Yes": 1, "No": 0}

# 🔹 Convert inputs
gender_val = gender_map[gender]
chol_val = chol_map[chol]
smoke_val = smoke_map[smoke]
glucose_val = glucose_map[glucose]
activity_val = activity_map[activity]
cvd_val = cvd_map[cvd]

# 🔹 Prepare model input

# prediction = grid.predict(X)[0]



if st.button("🔍 Predict Blood Pressure"):
    if gender and chol and smoke and glucose and activity and cvd:
        try:
            X = np.array([gender_val,chol_val, glucose_val, smoke_val,activity_val,    cvd_val,age, bmi]).reshape(1,-1)
            prediction = grid.predict(X)[0]
            st.success(f"✅ Predicted Arterial Pressure: {prediction:.2f} mmHg")

        except:
            st.error("⚠️ Please enter valid numbers for Age, Height, and Weight.")
    else:
        st.warning("⚠️ Please fill in all the fields before prediction.")