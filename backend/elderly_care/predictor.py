import joblib
import numpy as np

class EnhancedMLHealthRiskPredictor:
    def __init__(self):
        # Load the trained model and scaler
        self.model = joblib.load("model.pkl")  # Path to your model file
        self.scaler = joblib.load("scaler.pkl")  # Path to your scaler file
        self.features = [
            'heart_rate', 'systolic_bp', 'diastolic_bp', 'blood_sugar', 'body_temperature',
            'bmi', 'respiratory_rate', 'age'
        ]

    def predict_risk(self, current_data):
        # Convert current data into the required format
        X = np.array([[current_data[f] for f in self.features]])
        # Scale the data using the loaded scaler
        X_scaled = self.scaler.transform(X)
        # Predict the probabilities and risk level
        risk_probabilities = self.model.predict_proba(X_scaled)[0]
        risk_level = self.model.predict(X_scaled)[0]
        return risk_level, risk_probabilities
