**Deployment link**  
https://loan-status-prediction-ixcy5yvjdqodon7gykwztj.streamlit.app/

# 🏦 Loan Status Prediction Using Machine Learning

## 📌 Definition

This project aims to predict whether a loan application will be **approved** or **not approved** based on various applicant details such as gender, marital status, income, education, credit history, and other relevant features.

---

## 🎯 Problem Statement

Financial institutions and banks receive thousands of loan applications daily. Assessing each application manually is time-consuming, costly, and prone to human bias.  

The goal of this project is to build a **machine learning model** that predicts the **loan approval status** (`Loan_Status`) for new applications, helping automate the screening process and assist loan officers in making informed decisions faster and more reliably.

---

## 🔍 Dataset Information

The dataset contains information about past loan applicants with the following features:

| Feature | Description |
| ------- | ----------- |
| **Loan_ID** | Unique Loan ID (not used for prediction) |
| **Gender** | Applicant gender (Male/Female) |
| **Married** | Whether applicant is married (Y/N) |
| **Dependents** | Number of dependents (0,1,2,3+) |
| **Education** | Graduate or Not Graduate |
| **Self_Employed** | Self-employed or not (Y/N) |
| **ApplicantIncome** | Monthly income of applicant |
| **CoapplicantIncome** | Monthly income of co-applicant |
| **LoanAmount** | Loan amount (in thousands) |
| **Loan_Amount_Term** | Term of loan (in months) |
| **Credit_History** | Meets credit guidelines (1) or not (0) |
| **Property_Area** | Urban / Semi Urban / Rural |
| **Loan_Status** | Loan approved (Y) or not approved (N) |

---

## 📊 Exploratory Data Analysis (EDA)

- Checked for missing values and handled them using mode or by dropping rows with critical missing fields.
- Converted categorical features to numerical using **label encoding** and **mapping**.
- Scaled numerical columns (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`, `Loan_Amount_Term`) using **StandardScaler**.
- Visualized distributions to understand trends in loan approvals.

---

## 🤖 Model Building

Several algorithms were trained and evaluated:
- **Logistic Regression**
- **Support Vector Machine (SVC)**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Gradient Boosting Classifier**

All models were validated using **train/test split** and **K-Fold Cross Validation** to ensure robust performance.
----
## Results

| Model               | Accuracy (CV Avg) |
| ------------------- | ----------------- |
| Logistic Regression | 80.48%            |
| SVC                 | 80.66%            |
| Decision Tree       | 70.89%            |
| Random Forest       | 80.66%            |
| Gradient Boosting   | 77.4%             |


**Best Result:**  
The **Random Forest Classifier** with hyperparameter tuning gave the best cross-validation score (~80.66%) and balanced performance, handling non-linearities and feature importance well.

---

## ✅ Why Random Forest?

- **Handles missing values and outliers well**
- **Works with both categorical and numerical data**
- **Reduces overfitting** by averaging multiple trees
- **Interpretable feature importance**
- Good balance of **accuracy** and **speed**

This makes it an ideal choice for production-level deployment for structured tabular data like this loan dataset.

---

## 🚀 Model Deployment

The final tuned Random Forest model was saved using **joblib** (`loan_status_predict`).

A simple **Streamlit web app** was created to deploy this model. Users can input applicant details through a user-friendly interface and get instant loan approval predictions.

---

## 💡 Conclusion
Using machine learning, we built a reliable loan status prediction system. This tool can help banks and financial institutions streamline the loan approval process and make quick, data-driven decisions.






