# Home Loan Default Prediction

## Project Overview

This project aims to predict whether a customer will default on a home loan using machine learning techniques. Financial institutions need reliable models to identify high-risk customers before approving loans. By analyzing customer financial behavior, credit history, and previous loan records, this project builds predictive models to estimate the probability of loan default.

The project uses multiple relational datasets and combines them through aggregation to create a comprehensive feature set for modeling.

---

# Problem Statement

Banks and lending institutions face significant financial risk when customers fail to repay loans. Predicting potential loan defaulters helps institutions:

* Reduce financial losses
* Improve risk assessment
* Make better loan approval decisions

The objective of this project is to build a machine learning model that predicts whether a loan applicant will default based on historical financial and credit data.

---

# Dataset Description

The dataset consists of multiple related tables containing customer financial and credit information.

### 1. application_train

Main dataset containing loan application details for each customer.

Key features include:

* Income
* Loan amount
* Employment details
* Family status
* Housing information
* Credit history

Target variable:

TARGET
0 → Loan repaid
1 → Loan default

---

### 2. bureau

Contains historical credit records reported to the credit bureau.

Includes information such as:

* Credit status
* Credit duration
* Loan amount
* Overdue payments

---

### 3. bureau_balance

Monthly balance status of loans reported in the bureau dataset.

---

### 4. previous_application

Contains information about previous loan applications submitted by customers.

---

### 5. credit_card_balance

Contains monthly credit card balance information.


---

# Project Workflow

The project follows a structured machine learning pipeline.

Data Loading
↓
Initial Data Exploration
↓
Feature Engineering
↓
Dataset Aggregation (multiple datasets combined)
↓
Missing Value Handling
↓
Exploratory Data Analysis (EDA)
↓
Feature Selection
↓
Train-Test Split
↓
Encoding Categorical Variables
↓
Feature Scaling
↓
Class Imbalance Handling (SMOTE)
↓
Model Training
↓
Hyperparameter Tuning
↓
Model Evaluation and Comparison

---

# Dataset Aggregation

Since the project includes multiple relational datasets, aggregation was performed before modeling.

Group-by operations were applied to summarize customer financial behavior. Aggregation techniques used include:

* Mean
* Sum
* Count
* Max
* Min

The following datasets were aggregated and merged with the main application dataset:

* Bureau records
* Previous loan applications
* Installment payment history
* Credit card balances
* POS cash balances

This step creates a comprehensive dataset that captures the customer’s financial history.

---

# Exploratory Data Analysis (EDA)

EDA was performed to understand patterns in the data and identify important relationships.

Key analyses include:

* Target variable distribution
* Income distribution
* Loan amount distribution
* Age analysis
* Gender vs loan default
* Education level vs loan default
* Correlation heatmap
* Outlier detection

Visualization libraries used:

Matplotlib
Seaborn

---

# Data Preprocessing

Several preprocessing techniques were applied before training the models.

### Handling Missing Values

Missing values were analyzed and filled using appropriate strategies such as median imputation.

### Encoding Categorical Variables

Categorical features were converted into numerical format using:

* Label Encoding
* One-Hot Encoding

### Feature Scaling

Numerical features were standardized using:

StandardScaler

This ensures that features have comparable scales for model training.

---

# Handling Class Imbalance

The dataset is highly imbalanced because the number of non-default cases is much higher than default cases.

To address this issue, the **SMOTE (Synthetic Minority Oversampling Technique)** method was used to balance the dataset by generating synthetic samples for the minority class.

This helps improve the model's ability to detect loan defaults.

---

# Machine Learning Models Used

Multiple machine learning algorithms were trained and compared.

### Logistic Regression

A baseline linear classification model used for binary classification problems.

Advantages:

* Simple and interpretable
* Fast training
* Good baseline performance

---

### Random Forest

An ensemble learning method that builds multiple decision trees and combines their predictions.

Advantages:

* Handles nonlinear relationships
* Reduces overfitting
* Works well with large feature sets

Hyperparameter tuning was performed using RandomizedSearchCV.

---

### XGBoost

Extreme Gradient Boosting is an optimized gradient boosting algorithm widely used in machine learning applications.

Advantages:

* High predictive accuracy
* Handles missing values efficiently
* Built-in regularization

Hyperparameter tuning was performed using RandomizedSearchCV.

---

### LightGBM

Light Gradient Boosting Machine is designed for high performance on large datasets.

Advantages:

* Faster training
* Lower memory usage
* Strong performance on structured data

---

# Model Evaluation

The models were evaluated using several classification metrics.

Accuracy
Precision
Recall
F1 Score
ROC-AUC Score

These metrics help measure how well the models identify loan defaulters and non-defaulters.

---

# Model Comparison

All four models were trained and compared to determine the best-performing model. Performance metrics were analyzed to identify the algorithm that provides the best predictive performance.

Boosting models such as XGBoost and LightGBM often perform well on structured financial datasets.

---

# Technologies Used

Programming Language

Python

Libraries

Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
XGBoost
LightGBM
Imbalanced-learn (SMOTE)
Jupyter Notebook

---

# Results

Machine learning models were trained on aggregated financial datasets to predict loan default risk. Evaluation metrics such as ROC-AUC, precision, recall, and accuracy were used to assess model performance.

The models demonstrate the ability to identify customers with a higher probability of loan default.

---

# Future Improvements

Possible improvements include:

* Advanced feature engineering
* Cross-validation
* Feature importance analysis
* Model explainability using SHAP
* Hyperparameter optimization
* Model deployment using Flask or FastAPI
* Building an interactive dashboard

---

# Conclusion

This project demonstrates how machine learning techniques can be applied to financial risk prediction. By aggregating multiple datasets and applying advanced machine learning algorithms, the system can effectively predict loan default risk and assist financial institutions in making better lending decisions.
