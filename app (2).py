import streamlit as st
import joblib
import numpy as np

# Load the heart disease model
heart_disease_model = joblib.load('heart_disease_model.pkl')

# Title of the app
st.title("Heart Disease Prediction")

# Input fields for heart disease prediction
st.subheader("Enter Patient Information")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1])
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar", options=[0, 1,2])
restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2,3])
thalch = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1,2])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2,3])
ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia", options=[0, 1, 2, 3])

# Prediction button
if st.button("Predict Heart Disease"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalch, exang, oldpeak, slope, ca, thal]])
    prediction = heart_disease_model.predict(input_data)
    if prediction[0] == 0:
        st.success("Prediction: No heart disease")
    else:
        st.error(f"Prediction: Heart disease severity level {prediction[0]}")
