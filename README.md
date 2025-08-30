🏥 Medical Insurance Charges Prediction
📌 Project Overview

This project predicts medical insurance charges based on patient health and demographic details such as age, BMI, children, smoking status, sex, and region.

Machine learning regression models were applied, and their performance was compared. The goal is to understand how different factors (especially smoking) influence insurance costs and to build a predictive tool with a frontend using Streamlit.

📊 Dataset

Source: Medical Insurance Dataset

Features:

age → Age of the individual

sex → Gender (male/female)

bmi → Body Mass Index

children → Number of children covered by insurance

smoker → Smoking status (yes/no)

region → Residential region (northeast, northwest, southeast, southwest)

Target:

charges → Medical insurance cost (in USD)

🛠️ Methodology

Exploratory Data Analysis (EDA)

Visualized gender distribution, smoking distribution, boxplots for numerical features

Explored relationship between smoking and insurance charges

Preprocessing

One-hot encoding for categorical features

Feature scaling (Standardization)

Outlier detection using IQR

Modeling
Models used:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

XGBoost Regressor

Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

Cross Validation

5-fold cross validation used to check generalization

Hyperparameter Tuning

GridSearchCV applied to optimize XGBoost

📈 Results
Model	MAE	RMSE	R²
Linear Regression	2620.93	4458.44	0.63
Random Forest	2477.89	4493.05	0.62
Gradient Boosting	2480.32	4524.86	0.62
XGBoost (Tuned)	2431.00	4294.12	0.66

Gradient Boosting performed best under cross-validation.

XGBoost with tuning performed best on train/test split.

Smoking status had the largest impact on charges.

💻 Frontend (Streamlit App)

A simple web app built using Streamlit.

Users can input personal details (age, BMI, smoker status, etc.).

The trained model (saved with Pickle) predicts estimated insurance charges.

Run the app with:

streamlit run app.py

🚀 Key Learnings

Smoking increases insurance charges drastically.

Machine learning models can capture general trends but may under/overestimate individual cases.

Cross-validation provides a more reliable measure of performance than a single train/test split.

✅ Conclusion

This project demonstrates how regression models can predict medical insurance charges and how factors like smoking and BMI significantly impact costs. While models provide reasonable estimates, real-world insurance pricing involves more complex factors beyond this dataset.

