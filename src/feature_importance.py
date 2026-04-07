import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load saved model
model = joblib.load("models/random_forest_model.pkl")

print("Model loaded")

# Feature names
features = ["packet_size", "protocol"]

# Get importance
importance = model.feature_importances_

print("Feature Importance:")

for i in range(len(features)):
    print(features[i], ":", importance[i])

# Plot graph
plt.bar(features, importance)

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.show()