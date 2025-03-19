**Sales Forecasting Across Multiple Retail Stores**

This project aims to build an accurate Sales Forecasting System for Rossmann Pharmaceuticals using Machine Learning (ML) and Deep Learning techniques. The system predicts future sales for multiple retail stores over a 6-week period.


**Key Features**

✅ Predicts sales trends using historical data.
✅ Utilizes both Random Forest and LSTM Models for enhanced accuracy.
✅ Web interface for easy prediction and visualization.
✅ Tracks model performance using MLFlow.


**🔎 Data Preprocessing**

Handled missing values and outliers.

Extracted key date features (e.g., weekday, month-end).

Scaled data using StandardScaler for better model convergence.



**Models Used**
1. Random Forest Regressor
Implemented using Sklearn Pipelines
Feature Importance analysis improved model insights.
3. LSTM Model (Deep Learning)
Designed using TensorFlow/Keras.
Applied feature scaling with data transformed into supervised format.
Enhanced performance with time-series sliding window technique.

**Web App Deployment**

Built a user-friendly interface using Flask and Streamlit.

Enables users to:Upload CSV files.

View predicted sales and customer numbers.

Integrated MLFlow for tracking model versions and metrics.

**Results & Insights**

Achieved improved forecasting accuracy by incorporating: 

✅ Promo effects

✅ Seasonal trends

✅ Competitor distance impact

**Dependencies**

Python 3.10

TensorFlow/Keras

Scikit-learn

Pandas, NumPy

Flask/Streamlit

MLFlow

