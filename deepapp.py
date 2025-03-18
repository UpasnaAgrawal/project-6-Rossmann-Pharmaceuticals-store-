import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the trained model
with open('lstm_sales_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("LSTM Sales Prediction App")

# Input Fields
st.sidebar.header("Input Features")

def user_input_features():
    store = st.sidebar.number_input('Store', min_value=1, step=1)
    day_of_week = st.sidebar.number_input('Day of Week', min_value=1, max_value=7)
    date = st.sidebar.date_input('Date')
    customers = st.sidebar.number_input('Customers', value=0)
    open_status = st.sidebar.selectbox('Open Status', [0, 1])
    promo = st.sidebar.selectbox('Promo', [0, 1])
    state_holiday = st.sidebar.selectbox('State Holiday', [0, 1])
    school_holiday = st.sidebar.selectbox('School Holiday', [0, 1])

    features = np.array([[
        store, day_of_week, customers, open_status,
        promo, state_holiday, school_holiday
    ]]).reshape(1, 1, -1)

    return features
features = user_input_features()

# Prediction
if st.sidebar.button("Predict"):
    try:
        prediction = model.predict(features)
        st.success(f"Predicted Sales: {float(prediction[0][0]):.2f}")
    except Exception as e:
        st.error(f"Error: {e}")