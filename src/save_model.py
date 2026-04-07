import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("data/traffic.csv")

# Convert protocol to numbers
data["protocol"] = data["protocol"].map({
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
})

# Features and Label
X = data[["packet_size", "protocol"]]
y = data["label"]

# Encode labels to numbers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train model
model = DecisionTreeClassifier()
model.fit(X, y_encoded)

# Save model and encoder
joblib.dump(model, "models/dpi_model.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("Model saved successfully")