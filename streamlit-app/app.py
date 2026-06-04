import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.markdown("""
# 🏦 Loan Approval Prediction System

Predict whether a customer loan application is likely to be approved or rejected using a Decision Tree Machine Learning model.
""")

st.info("Fill in the applicant details and click Predict Loan Status.")

loan_data = pd.read_csv("dataset/loan_approval_decision_tree_dataset.csv")

employment_encoder = LabelEncoder()
education_encoder = LabelEncoder()
loan_status_encoder = LabelEncoder()

loan_data["Employment_Status"] = employment_encoder.fit_transform(loan_data["Employment_Status"])
loan_data["Education_Level"] = education_encoder.fit_transform(loan_data["Education_Level"])
loan_data["Loan_Status"] = loan_status_encoder.fit_transform(loan_data["Loan_Status"])

X = loan_data.drop("Loan_Status", axis=1)
y = loan_data["Loan_Status"]

loan_model = DecisionTreeClassifier(criterion="gini", random_state=42)
loan_model.fit(X, y)

annual_income = st.number_input("Annual Income", min_value=0, value=500000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=750)
loan_amount = st.number_input("Loan Amount", min_value=0, value=200000)

employment_status = st.selectbox(
    "Employment Status",
    employment_encoder.classes_
)

education_level = st.selectbox(
    "Education Level",
    education_encoder.classes_
)

existing_debt = st.number_input("Existing Debt", min_value=0, value=50000)

if st.button("Predict Loan Status"):

    employment_encoded = employment_encoder.transform([employment_status])[0]
    education_encoded = education_encoder.transform([education_level])[0]

    applicant_data = pd.DataFrame({
        "Annual_Income": [annual_income],
        "Credit_Score": [credit_score],
        "Loan_Amount": [loan_amount],
        "Employment_Status": [employment_encoded],
        "Education_Level": [education_encoded],
        "Existing_Debt": [existing_debt]
    })

    prediction = loan_model.predict(applicant_data)

    final_result = loan_status_encoder.inverse_transform(prediction)[0]

    if final_result == "Approved":
        st.success("✅ Loan Application Status: Approved")
    else:
        st.error("❌ Loan Application Status: Rejected")