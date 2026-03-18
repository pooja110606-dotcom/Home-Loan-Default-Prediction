# Project Summary: Home Loan Default Prediction

## Business Problem

Financial institutions face significant risk when customers fail to repay loans. Identifying high-risk customers before loan approval is critical to reduce financial losses.

This project aims to predict whether a customer will default on a home loan using historical financial and credit data.

---

## Objective

To build a machine learning model that can accurately predict loan default risk and support better decision-making in lending.

---

## Data Overview

The project uses multiple datasets:

- Application data (customer details)
- Bureau data (credit history)
- Previous applications
- Installment payments
- Credit card balance
- POS cash balance

These datasets were aggregated to create a comprehensive view of each customer.

---

## Approach

The project follows a structured machine learning pipeline:

1. Data Loading  
2. Dataset Aggregation (multiple data sources combined)  
3. Feature Engineering  
4. Data Preprocessing  
5. Handling Class Imbalance using SMOTE  
6. Train-Test Split  
7. Model Training  
8. Model Evaluation  

---

## Models Used

- Logistic Regression  
- Random Forest  
- XGBoost  
- LightGBM  

---

## Key Challenges

- Highly imbalanced dataset (very few defaults)
- Large number of features from multiple datasets
- Data preprocessing complexity

---

## Solution Strategy

- Used SMOTE to handle class imbalance  
- Applied feature engineering to improve predictive power  
- Used ensemble models (Random Forest, XGBoost, LightGBM)  
- Compared multiple models for best performance  

---

## Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC Score  

Special focus was given to **Recall**, as identifying defaulters is critical.

---

## Key Insights

- Class imbalance significantly affects model performance  
- Feature engineering improves prediction accuracy  
- Boosting models (XGBoost, LightGBM) perform better than basic models  
- Aggregated financial history plays a key role in prediction  

---

## Business Impact

- Helps banks identify high-risk customers  
- Reduces financial loss due to defaults  
- Improves loan approval decisions  
- Enables risk-based customer segmentation  

---

## Conclusion

This project demonstrates how machine learning can be used to predict loan default risk using structured financial data. The developed models provide valuable insights that can help financial institutions make better lending decisions.

---

## Future Improvements

- Hyperparameter tuning optimization  
- Feature importance analysis  
- Model explainability (SHAP)  
- Model deployment (API or dashboard)  
