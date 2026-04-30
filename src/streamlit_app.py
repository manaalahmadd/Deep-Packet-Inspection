import random
import time

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DPI Detector", layout="centered")

st.title("DPI Packet Detection System")
st.markdown("Real-time network packet analysis using Machine Learning")

# Load model
model = joblib.load("models/random_forest_model.pkl")

# Input fields
packet_size = st.number_input("Enter Packet Size", value=100)
protocol = st.selectbox("Select Protocol", ["TCP", "UDP", "ICMP"])

# Convert protocol
protocol_map = {"TCP": 1, "UDP": 2, "ICMP": 3}
protocol_num = protocol_map[protocol]

# Predict button
if st.button("Predict"):
    data = pd.DataFrame(
        {
            "packet_size": [packet_size],
            "protocol": [protocol_num],
        }
    )

    result = model.predict(data)[0]
    if result == "Suspicious":
        st.error("ALERT: Suspicious Packet Detected!")
    else:
        st.success("✅ Normal Packet")

st.subheader("Data Visualization")

# Sample data (ya tum CSV se bhi le sakte ho)
data = pd.read_csv("data/traffic.csv")

# Packet size graph
st.write("Packet Size Distribution")
plt.figure()
plt.hist(data["packet_size"])
st.pyplot(plt)

# Protocol count
st.write("Protocol Usage")
protocol_counts = data["protocol"].value_counts()
plt.figure()
protocol_counts.plot(kind="bar")
st.pyplot(plt)

st.write("Protocol Pie Chart")
protocol_counts.plot(kind="pie", autopct="%1.1f%%")
st.pyplot(plt)

st.subheader("Live Packet Simulation")

if st.button("Start Simulation"):
    protocol_map = {1: "TCP", 2: "UDP", 3: "ICMP"}

    for i in range(10):  # 10 packets simulate
        packet_size = random.randint(40, 1800)
        protocol_num = random.choice([1, 2, 3])

        data = pd.DataFrame(
            {
                "packet_size": [packet_size],
                "protocol": [protocol_num],
            }
        )

        prediction = model.predict(data)[0]

        st.write(f"Packet {i+1}")
        st.write(f"Size: {packet_size}")
        st.write(f"Protocol: {protocol_map[protocol_num]}")
        st.write(f"Prediction: {prediction}")
        st.write("------")

        time.sleep(1)
