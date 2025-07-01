import streamlit as st
import joblib
import pandas as pd

# Load model once to avoid reloading on every run
model = joblib.load('loan_status_predict')

# App title
st.title("Loan Status Prediction Using Machine Learning")

# Instructions
st.write("""
Please enter the following details to predict if your loan will be approved.
""")

# Input fields
p1 = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x==1 else "Female")
p2 = st.selectbox("Married", [1, 0], format_func=lambda x: "Yes" if x==1 else "No")
p3 = st.selectbox("Dependents", [1, 2, 3, 4])
p4 = st.selectbox("Education", [1, 0], format_func=lambda x: "Graduate" if x==1 else "Not Graduate")
p5 = st.selectbox("Self Employed", [1, 0], format_func=lambda x: "Yes" if x==1 else "No")
p6 = st.number_input("Applicant Income", min_value=0.0)
p7 = st.number_input("Coapplicant Income", min_value=0.0)
p8 = st.number_input("Loan Amount", min_value=0.0)
p9 = st.number_input("Loan Amount Term", min_value=0.0)
p10 = st.selectbox("Credit History", [1, 0], format_func=lambda x: "Good" if x==1 else "Bad")
p11 = st.selectbox("Property Area", [1, 2, 3], format_func=lambda x: {1: "Urban", 2: "Semiurban", 3: "Rural"}[x])

# Predict button
if st.button("Predict Loan Status"):
    df = pd.DataFrame({
        'Gender': [p1],
        'Married': [p2],
        'Dependents': [p3],
        'Education': [p4],
        'Self_Employed': [p5],
        'ApplicantIncome': [p6],
        'CoapplicantIncome': [p7],
        'LoanAmount': [p8],
        'Loan_Amount_Term': [p9],
        'Credit_History': [p10],
        'Property_Area': [p11]
    })

    result = model.predict(df)

    if result[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
