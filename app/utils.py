import joblib
import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model and scaler only once
model = joblib.load(BASE_DIR / "models" / "logistic_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")


def predict_customer(time_site, age, income, internet, male):
    """
    Predict whether a customer will click an advertisement.

    Returns:
        prediction (0 or 1)
        probability (float)
    """

    # Create dataframe
    input_data = pd.DataFrame({
        "Daily Time Spent on Site": [time_site],
        "Age": [age],
        "Area Income": [income],
        "Daily Internet Usage": [internet],
        "Male": [male]
    })

    # Scale only numerical columns
    numerical_features = [
        "Daily Time Spent on Site",
        "Age",
        "Area Income",
        "Daily Internet Usage"
    ]

    scaled = scaler.transform(input_data[numerical_features])

    final_input = pd.DataFrame(
        scaled,
        columns=numerical_features
    )

    # Add Male without scaling
    final_input["Male"] = input_data["Male"].values

    # Prediction
    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0][1]

    return prediction, probability