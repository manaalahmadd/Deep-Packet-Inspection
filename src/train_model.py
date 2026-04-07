import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = pd.read_csv("data/traffic.csv")

# Step 2: Convert protocol to numbers
data["protocol"] = data["protocol"].map({
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
})

# Step 3: Features and Label
X = data[["packet_size", "protocol"]]
y = data["label"]

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create model
model = DecisionTreeClassifier()

# Step 6: Train model
model.fit(X_train, y_train)

# Step 7: Predict
predictions = model.predict(X_test)

# Step 8: Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100)