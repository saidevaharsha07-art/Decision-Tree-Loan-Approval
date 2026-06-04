# 🏦 Loan Approval Prediction Using Decision Tree

## 📌 Project Overview

Loan approval is an important process in the banking and financial sector. Evaluating applications manually can be time-consuming and may lead to inconsistent decisions.

This project implements a **Loan Approval Prediction System** using the **Decision Tree Machine Learning Algorithm**. The model predicts whether a customer's loan application is likely to be approved or rejected based on factors such as income, credit score, loan amount, employment status, education level, and existing debt.

---

## 🎯 Problem Statement

Banks and financial institutions must evaluate customer loan applications before approval. This process depends on several factors such as annual income, credit score, loan amount, employment status, education level, and existing debt.

The objective of this project is to build a Decision Tree Machine Learning model that predicts whether a customer's loan application will be approved or rejected based on these factors. This helps automate the loan evaluation process and supports faster decision-making.

---

## 📂 Dataset Information

The dataset contains **200 records** and **7 features**.

### Features

| Feature | Description |
|----------|-------------|
| Annual_Income | Applicant's annual income |
| Credit_Score | Applicant's credit score |
| Loan_Amount | Requested loan amount |
| Employment_Status | Employment category |
| Education_Level | Educational qualification |
| Existing_Debt | Current debt amount |
| Loan_Status | Approved / Rejected |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Jupyter Notebook

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Loading
- Imported dataset using Pandas.
- Inspected dataset structure and features.

### 2️⃣ Data Preprocessing
- Checked missing values.
- Encoded categorical variables using Label Encoding.

### 3️⃣ Feature Selection
- Selected relevant features for prediction.
- Defined target variable.

### 4️⃣ Model Training
- Split dataset into training and testing sets.
- Trained a Decision Tree Classifier.

### 5️⃣ Model Evaluation
- Accuracy Score
- Classification Report
- Confusion Matrix

### 6️⃣ Data Visualization
- Decision Tree Visualization
- Feature Importance Graph
- Correlation Heatmap

### 7️⃣ Streamlit Deployment
- Built an interactive web application for real-time loan approval prediction.

---

## 📊 Model Performance

### Accuracy

```text
97.5%
```

The Decision Tree model achieved an accuracy of **97.5%** on the testing dataset.

---

## 🖥️ Streamlit Application

The application allows users to:

- Enter applicant details
- Predict loan approval status
- Receive instant prediction results

### Inputs

- Annual Income
- Credit Score
- Loan Amount
- Employment Status
- Education Level
- Existing Debt

### Output

```text
✅ Approved
❌ Rejected
```

---

## 📸 Project Screenshots

### Loan Approval Prediction App

(Add Streamlit Screenshot Here)

### Confusion Matrix

(Add Screenshot Here)

### Decision Tree Visualization

(Add Screenshot Here)

### Feature Importance Graph

(Add Screenshot Here)

---

## 📁 Project Structure

```text
03-Decision-Tree-Loan-Approval
│
├── dataset
│   └── loan_approval_decision_tree_dataset.csv
│
├── notebooks
│   └── Loan_Approval_Decision_Tree.ipynb
│
├── reports
│
├── screenshots
│
├── streamlit-app
│   └── app.py
│
└── README.md
```

---

## 🚀 Future Improvements

- Random Forest Classifier
- Hyperparameter Tuning
- Model Deployment on Cloud
- Larger Real-World Dataset
- Advanced Loan Risk Analysis

---

## 👨‍💻 Author

**Sai Deva Harsha**

AI & ML Internship Project

GitHub: https://github.com/saidevaharsha07-art
