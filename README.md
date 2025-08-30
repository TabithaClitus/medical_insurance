APP LINK:https://medicalinsurance-wfhnpdzcdiqunhukdvj7yt.streamlit.app/

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

🎯MODELS USED:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

XGBoost Regressor

🎯EVALUATION METRICS:

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

VISUALIZATION:

<img width="509" height="504" alt="image" src="https://github.com/user-attachments/assets/16d45995-99be-49bc-baf3-44e6ba85697e" />

<img width="481" height="504" alt="image" src="https://github.com/user-attachments/assets/34892000-0a81-4fb4-a892-f7071c53b6fd" />

<img width="1189" height="790" alt="image" src="https://github.com/user-attachments/assets/b39e3c67-99e3-4ded-afaf-fb38ce289e47" />

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/e396c29c-ab20-4485-a07c-1baca43c9a79" />

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/f2e3de77-ffec-422a-ae59-c6c0736bf404" />

<img width="868" height="547" alt="image" src="https://github.com/user-attachments/assets/4f5cc1cf-7a54-4f82-8836-a9b019947a4c" />

<img width="605" height="445" alt="image" src="https://github.com/user-attachments/assets/b3a1befd-a7f7-46c7-8dca-a63644adf770" />

<img width="540" height="547" alt="image" src="https://github.com/user-attachments/assets/f15770e5-8229-417d-b334-ad5a0bcf42f9" />

<img width="571" height="501" alt="image" src="https://github.com/user-attachments/assets/4776e2cd-15a7-42a6-9a9f-b62039ac758f" />

<img width="1023" height="593" alt="image" src="https://github.com/user-attachments/assets/636af5d5-4e2f-4e4d-8db7-08469229856b" />

<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/292c327c-554b-43ca-a08c-209e61d611a8" />

<img width="859" height="579" alt="image" src="https://github.com/user-attachments/assets/dd0e5271-32bc-47d1-8058-e9cdd675b3bf" />

<img width="691" height="502" alt="image" src="https://github.com/user-attachments/assets/6b6f9818-3c58-417d-afda-15ea54cdbfcc" />

<img width="649" height="624" alt="image" src="https://github.com/user-attachments/assets/5bb6bcdc-4620-41d0-85c0-1ad02121e39d" />

✅ Conclusion

This project demonstrates how regression models can predict medical insurance charges and how factors like smoking and BMI significantly impact costs. While models provide reasonable estimates, real-world insurance pricing involves more complex factors beyond this dataset.

