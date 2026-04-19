import joblib
import pandas as pd
from datetime import datetime

# Load model
model = joblib.load("models/random_forest_model.pkl")

print("=== DPI Packet Simulator with Logging ===")

# Input
packet_size = int(input("Enter packet size: "))
protocol_name = input("Enter protocol (TCP/UDP/ICMP): ")

# Convert protocol
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

protocol = protocol_map.get(protocol_name.upper())

# DataFrame
new_data = pd.DataFrame({
    "packet_size": [packet_size],
    "protocol": [protocol]
})

# Prediction
prediction = model.predict(new_data)[0]

print("Prediction:", prediction)

# Create log entry
log_data = pd.DataFrame({
    "time": [datetime.now()],
    "packet_size": [packet_size],
    "protocol": [protocol_name.upper()],
    "prediction": [prediction]
})

# Save to CSV (append mode)
log_data.to_csv("logs.csv", mode='a', header=False, index=False)

print("Log saved successfully")