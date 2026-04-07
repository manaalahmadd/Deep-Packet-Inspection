import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("data/traffic.csv")

# Convert protocol to numbers
data["protocol"] = data["protocol"].map({
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
})

# Features and label
X = data[["packet_size", "protocol"]]
y = data["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
packet_size = int(input("Enter Packet Size: "))
protocol = input("Enter Protocol (TCP/UDP/ICMP): ")

# Convert protocol
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

protocol_number = protocol_map.get(protocol.upper())

# Prediction
input_data = pd.DataFrame([[packet_size, protocol_number]], columns=["packet_size", "protocol"])
prediction = model.predict(input_data)

print("Prediction:", prediction[0])