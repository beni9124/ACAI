#Prediction and Maintenance Scheduling for Aviation Components using Machine Learning
# This script simulates sensor data from aviation components, trains a machine learning model to predict failures, and demonstrates how to use the model for predictions.


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler


# 1. Simulate sensor data for aviation components
def generate_sample_data(n_samples=1000):
    np.random.seed(42)
    data = {
        'temperature': np.random.normal(70, 10, n_samples),
        'vibration': np.random.normal(0.5, 0.1, n_samples),
        'pressure': np.random.normal(30, 5, n_samples),
        'runtime_hours': np.random.normal(500, 100, n_samples),
        'error_count': np.random.poisson(2, n_samples),
        "product_id": np.random.randint(1000, 1100, n_samples),
        "supplier historical data": np.random.randint(0, 2, n_samples)
    }
    # Simulate failure: higher temp, vibration, error_count increase failure chance
    failure_prob = (
        0.2 * (data['temperature'] > 80) +
        0.3 * (data['vibration'] > 0.6) +
        0.2 * (data['error_count'] > 3) +
        0.1 * (data['pressure'] < 25) +
        0.2 * (data['runtime_hours'] > 600) +
        0.4 * (data['product_id'] == 1001) +
        0.3 * (data['supplier historical data'] == 1)
    )
    data['failure'] = (np.random.rand(n_samples) < failure_prob).astype(int)
    return pd.DataFrame(data)

# 2. Preprocess data
def preprocess_data(df):
    X = df.drop('failure', axis=1)
    y = df['failure']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler

# 3. Train model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
    print('\nClassification Report:\n', classification_report(y_test, y_pred))
    return model

# 4. Predict on new data
def predict_failure(model, scaler, new_data):
    X_new = scaler.transform(new_data)
    return model.predict(X_new)

if __name__ == "__main__":
    # Generate and preprocess data
    df = generate_sample_data()
    X, y, scaler = preprocess_data(df)
    # Train model
    model = train_model(X, y)
    # Example prediction
    new_sensor_data = pd.DataFrame({
        'temperature': [85],
        'vibration': [0.7],
        'pressure': [28],
        'runtime_hours': [650],
        'error_count': [5],
        'product_id': [1001],
        'supplier historical data': [1]
    })
    prediction = predict_failure(model, scaler, new_sensor_data)
    if prediction >= 0.5:
        prediction = 1
    else: prediction = 0
    if prediction == 1:
        print("Warning: Component is likely to fail soon. Schedule maintenance.")
    else:
        print("Component is operating normally.")
    # Schedule maintenance (simple demonstration)
    print("Enter date of maintenance (YYYY-MM-DD):")
    maintenance_date = input()
    print(f"Maintenance scheduled for {maintenance_date}.")
    print("Notify maintenance team.")
    send_email = input("Enter 'y' to send email notification to maintenance team: ")
    if send_email.lower() != 'y':
        print("Enter email address:")
        email_address = input()
        print(f"Sending email to {email_address} about scheduled maintenance on {maintenance_date}.")
