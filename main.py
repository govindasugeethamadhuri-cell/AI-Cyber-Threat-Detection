from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib


app = FastAPI(title="AI Cyber Threat Detection API")


# Allow dashboard to connect to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Load AI model
model = joblib.load("ml/model.pkl")
encoder = joblib.load("ml/label_encoder.pkl")


# Risk levels
risk_levels = {
    "NORMAL": "LOW",
    "BRUTE_FORCE": "MEDIUM",
    "PORT_SCAN": "HIGH",
    "DOS": "CRITICAL",
    "DATA_EXFILTRATION": "CRITICAL"
}


# Evidence for each threat
evidence = {
    "NORMAL": "Normal traffic pattern",
    "BRUTE_FORCE": "High connection count on SSH port",
    "PORT_SCAN": "Multiple destination ports detected",
    "DOS": "Very high packet rate and traffic volume",
    "DATA_EXFILTRATION": "Large amount of data transferred"
}


@app.get("/")
def home():
    return {
        "message": "AI Cyber Threat Detection API is running"
    }


@app.get("/alerts")
def get_alerts():

    # Load traffic dataset
    df = pd.read_csv("data/traffic.csv")


    # Features used by AI
    features = [
        "destination_port",
        "duration",
        "packets",
        "bytes",
        "packet_rate",
        "connection_count"
    ]

    X = df[features]


    # AI prediction
    predictions = model.predict(X)

    probabilities = model.predict_proba(X)


    # Convert prediction numbers to threat names
    df["threat"] = encoder.inverse_transform(predictions)


    # Add confidence
    df["confidence"] = [
        round(max(probability) * 100, 2)
        for probability in probabilities
    ]


    # Add risk level
    df["risk_level"] = [
        risk_levels.get(threat, "UNKNOWN")
        for threat in df["threat"]
    ]


    # Add supporting evidence
    df["evidence"] = [
        evidence.get(threat, "Unknown traffic pattern")
        for threat in df["threat"]
    ]


    return df.to_dict(orient="records")