import joblib
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load model
model = joblib.load("models/random_forest_model.pkl")

# Window
root = tk.Tk()
root.title("DPI Packet Detector")
root.geometry("300x250")

# Labels
tk.Label(root, text="Packet Size").pack()
packet_entry = tk.Entry(root)
packet_entry.pack()

tk.Label(root, text="Protocol (TCP/UDP/ICMP)").pack()
protocol_entry = tk.Entry(root)
protocol_entry.pack()

# Prediction function
def predict():
    try:
        packet_size = int(packet_entry.get())
        protocol_name = protocol_entry.get().upper()

        protocol_map = {
            "TCP": 1,
            "UDP": 2,
            "ICMP": 3
        }

        if protocol_name not in protocol_map:
            messagebox.showerror("Error", "Invalid Protocol")
            return

        protocol = protocol_map[protocol_name]

        data = pd.DataFrame({
            "packet_size": [packet_size],
            "protocol": [protocol]
        })

        result = model.predict(data)[0]

        result_label.config(text="Prediction: " + result)

    except:
        messagebox.showerror("Error", "Invalid Input")

# Button
tk.Button(root, text="Predict", command=predict).pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run app
root.mainloop()