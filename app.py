import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. Load model and column order
with open("gbr_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("gbr_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.title("💰 Medical Insurance Cost Predictor")

# 2. User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# 3. Convert input into DataFrame
input_dict = {
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex": [sex],
    "smoker": [smoker],
    "region": [region]
}
input_df = pd.DataFrame(input_dict)

# 4. One-hot encode user input
input_encoded = pd.get_dummies(input_df, drop_first=True)

# 5. Align columns with training
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# 6. Prediction
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
