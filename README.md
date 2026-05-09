# Deep Packet Inspection — AI/ML Network Security System

An AI-powered network traffic classifier that detects suspicious packets in real time using Machine Learning. Built with Python, Scikit-learn, and Streamlit.

🔗 **Live Demo:** [deep-packet-inspection-1511.streamlit.app](https://deep-packet-inspection-1511.streamlit.app/)

---

## Overview

Deep Packet Inspection (DPI) is a technique used in network security to analyze network traffic beyond just the headers — examining the actual content of packets to detect threats. This project implements a machine learning approach to DPI, classifying network traffic as **Normal** or **Suspicious** in real time.
<img width="368" height="534" alt="image" src="https://github.com/user-attachments/assets/1fcbe748-f42c-4f4c-8bfc-1936956394c9" />

---

## Features

- 🔍 Real-time packet classification using a trained Random Forest model
- ⚙️ Hyperparameter tuning with GridSearchCV for optimal model performance
- 📊 Interactive Streamlit dashboard with live packet simulation
- 🚨 Alert system that flags suspicious traffic instantly
- 📁 Clean project structure separating data, models, and source code

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| ML | Scikit-learn, Random Forest, GridSearchCV |
| Data | Pandas |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |

---

## How It Works

1. Network packet data is loaded and preprocessed (protocol encoding, feature extraction)
2. A Random Forest classifier is trained on labelled traffic data (Normal / Suspicious)
3. GridSearchCV tunes hyperparameters (`n_estimators`, `max_depth`, `min_samples_split`) using 3-fold cross-validation
4. The best model is used to classify incoming packets in the Streamlit dashboard
5. Suspicious packets trigger an alert in the UI

---

## Project Structure

```
Deep-Packet-Inspection/
├── data/               # Traffic dataset (CSV)
├── models/             # Saved trained models
├── src/                # Source code (preprocessing, prediction logic)
├── templates/          # HTML templates
├── tuned_model.py      # Model training and hyperparameter tuning
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for deployment
└── Procfile            # Deployment configuration
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/manaalahmadd/Deep-Packet-Inspection.git
cd Deep-Packet-Inspection

# Install dependencies
pip install -r requirements.txt
```

### Run the dashboard

```bash
streamlit run src/app.py
```

### Train / retune the model

```bash
python tuned_model.py
```

---

## Dataset

The model is trained on a labelled network traffic dataset containing the following features:

| Feature | Description |
|---------|-------------|
| `packet_size` | Size of the network packet in bytes |
| `protocol` | Network protocol (TCP, UDP, ICMP) |
| `label` | Traffic classification — Normal or Suspicious |

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | — |
| Best Parameters | Tuned via GridSearchCV |
| Cross-validation folds | 3 |

> Replace the `—` above with your actual accuracy and F1 score after running `tuned_model.py`

---

## Future Improvements

- [ ] Add more features: port number, duration, bytes/sec, TCP flag counts
- [ ] Save and load model with `joblib` to avoid retraining on each run
- [ ] Add confusion matrix and F1 score to the dashboard
- [ ] Train on a larger real-world dataset (e.g. CICIDS2017)

---

## Author

**Manaal Ahmad**
- GitHub: [@manaalahmadd](https://github.com/manaalahmadd)
- Email: manaalahmad1234@gmail.com

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
