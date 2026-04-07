import joblib
import sys
import os

# Load model safely
model_path = "models/dpi_model.pkl"

if not os.path.exists(model_path):
    print("Error: Model file not found!")
    sys.exit()

model = joblib.load(model_path)

# Input handling
try:
    if len(sys.argv) == 3:
        packet_size = int(sys.argv[1])
        protocol_input = sys.argv[2].upper()
    else:
        packet_size = int(input("Enter packet size: "))
        protocol_input = input("Enter protocol (TCP/UDP/ICMP): ").upper()

    # Protocol mapping
    protocol_map = {
        "TCP": 1,
        "UDP": 2,
        "ICMP": 3
    }

    if protocol_input not in protocol_map:
        print("Invalid protocol! Use TCP, UDP, or ICMP.")
        sys.exit()

    protocol = protocol_map[protocol_input]

    # Prediction
    prediction = model.predict([[packet_size, protocol]])

    # Output formatting
    print("\n--- DPI Prediction Result ---")
    print(f"Packet Size: {packet_size}")
    print(f"Protocol: {protocol_input}")
    print(f"Prediction: {prediction[0]}")

except ValueError:
    print("Invalid input! Please enter correct numeric values.")