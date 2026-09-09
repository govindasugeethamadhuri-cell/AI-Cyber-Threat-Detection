import joblib
import pandas as pd


# Load the trained AI model
model = joblib.load("ml/model.pkl")
encoder = joblib.load("ml/label_encoder.pkl")


# New network traffic to test
traffic = pd.DataFrame([{
    "destination_port": 22,
    "duration": 2,
    "packets": 250,
    "bytes": 12000,
    "packet_rate": 125,
    "connection_count": 40
}])


# Select the same features used during training
features = [
    "destination_port",
    "duration",
    "packets",
    "bytes",
    "packet_rate",
    "connection_count"
]

X = traffic[features]


# Predict the threat
prediction = model.predict(X)[0]

# Get probability for each class
probabilities = model.predict_proba(X)[0]


# Convert number back to threat name
threat = encoder.inverse_transform([prediction])[0]


# Calculate confidence
confidence = max(probabilities) * 100


print("\n========== AI THREAT DETECTION ==========")
print("Detected Threat :", threat)
print("Confidence      :", round(confidence, 2), "%")
print("==========================================")