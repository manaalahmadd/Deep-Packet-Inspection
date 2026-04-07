import joblib
import os
import pandas as pd

# Check model file
model_path = "models/dpi_model.pkl"
encoder_path = "models/label_encoder.pkl"

if not os.path.exists(model_path):
    print("Error: Model file not found!")
    exit()

if not os.path.exists(encoder_path):
    print("Error: Label encoder file not found!")
    exit()

# Load model and encoder
model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# Protocol mapping
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

# Input handling
try:
    packet_size = int(input("Enter Packet Size: "))
    protocol = input("Enter Protocol (TCP/UDP/ICMP): ").upper()

    if protocol not in protocol_map:
        print("Invalid protocol! Use TCP, UDP, or ICMP.")
        exit()

    protocol_number = protocol_map[protocol]

    # Prediction
    input_data = pd.DataFrame([[packet_size, protocol_number]], columns=["packet_size", "protocol"])
    prediction_encoded = model.predict(input_data)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)

    print("\n--- DPI Prediction ---")
    print(f"Packet Size: {packet_size}")
    print(f"Protocol: {protocol}")
    print(f"Prediction: {prediction_label[0]}")

except ValueError:
    print("Invalid input! Packet size must be a number.")