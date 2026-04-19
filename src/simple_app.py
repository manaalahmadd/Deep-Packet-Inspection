from flask import Flask, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return """
    <h2>DPI Packet Detector</h2>
    <form action="/predict" method="post">
        Packet Size: <input type="text" name="packet_size"><br><br>
        Protocol: <input type="text" name="protocol"><br><br>
        <input type="submit" value="Predict">
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    try:
        packet_size = int(request.form["packet_size"])
        protocol_name = request.form["protocol"].upper()

        protocol_map = {"TCP": 1, "UDP": 2, "ICMP": 3}

        if protocol_name not in protocol_map:
            return "Invalid Protocol"

        protocol = protocol_map[protocol_name]

        data = pd.DataFrame({
            "packet_size": [packet_size],
            "protocol": [protocol]
        })

        result = model.predict(data)[0]

        return f"<h3>Prediction: {result}</h3>"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=False, port=5000)