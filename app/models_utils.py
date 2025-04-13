import joblib
import os
import pandas as pd

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "planet_classifier.pkl")
model = joblib.load(model_path)

def predict_planet(features):
    feature_names = ['radius_km', 'mass_10^24kg', 'orbital_period_days', 'temperature_avg_c']
    input_data = pd.DataFrame([features], columns=feature_names)

    print(input_data)

    return model.predict([input_data])[0] 