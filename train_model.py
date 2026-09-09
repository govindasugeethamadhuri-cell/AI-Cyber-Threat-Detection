import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load the traffic dataset
df = pd.read_csv("data/traffic.csv")

print("Dataset loaded successfully!")
print("Total records:", len(df))


# Select features for AI
features = [
    "destination_port",
    "duration",
    "packets",
    "bytes",
    "packet_rate",
    "connection_count"
]

X = df[features]
y = df["label"]


# Convert threat names into numbers
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)


# Create the Random Forest AI model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
print("\nTraining AI model...")
model.fit(X_train, y_train)


# Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_
    )
)


# Save the trained model
joblib.dump(model, "ml/model.pkl")
joblib.dump(encoder, "ml/label_encoder.pkl")

print("\nAI model saved successfully!")
print("Model file: ml/model.pkl")
print("Encoder file: ml/label_encoder.pkl")