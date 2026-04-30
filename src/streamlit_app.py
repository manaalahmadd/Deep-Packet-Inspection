import random
import time

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DPI Detector", layout="centered")

st.title("AI-Based Deep Packet Inspection System")
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

# Sample data
data = pd.read_csv("data/traffic.csv")

# Packet size graph with selected input marker
st.write("Packet Size Distribution")
fig, ax = plt.subplots()
ax.hist(data["packet_size"], bins=20, color="skyblue", edgecolor="black", alpha=0.75)
ax.axvline(packet_size, color="red", linestyle="--", linewidth=2, label=f"Selected size: {packet_size}")
ax.set_xlabel("Packet size")
ax.set_ylabel("Count")
ax.set_title("Packet Size Distribution")
ax.legend()
st.pyplot(fig)

# Protocol count
st.write("Protocol Usage")
protocol_counts = data["protocol"].value_counts().reindex(["TCP", "UDP", "ICMP"]).fillna(0)
fig2, ax2 = plt.subplots()
protocol_counts.plot(kind="bar", ax=ax2, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
ax2.set_xlabel("Protocol")
ax2.set_ylabel("Count")
ax2.set_title("Protocol Usage")
st.pyplot(fig2)

st.write("Protocol Pie Chart")
fig3, ax3 = plt.subplots()
protocol_counts.plot(kind="pie", ax=ax3, autopct="%1.1f%%", startangle=90, ylabel="")
ax3.set_title("Protocol Distribution")
st.pyplot(fig3)

st.subheader("Live Packet Simulation")

if st.button("Start Simulation"):
    protocol_map = {1: "TCP", 2: "UDP", 3: "ICMP"}
    normal_count = 0
    suspicious_count = 0

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

        if prediction == "Normal":
            normal_count += 1
        else:
            suspicious_count += 1

        st.write(f"Packet {i+1}")
        st.write(f"Size: {packet_size}")
        st.write(f"Protocol: {protocol_map[protocol_num]}")
        st.write(f"Prediction: {prediction}")
        st.write("------")

        time.sleep(1)

    st.write(f"Total Normal Packets: {normal_count}")
    st.write(f"Total Suspicious Packets: {suspicious_count}")
