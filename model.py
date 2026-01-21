import pandas as pd
from sklearn.linear_model import LogisticRegression

# Sample training data
# Features: [amount, hour, merchant_type]
# merchant_type: 0 = Online, 1 = Store, 2 = International
X = [
    [50, 14, 1],
    [200, 10, 1],
    [500, 2, 2],
    [20, 18, 0],
    [1000, 1, 2],
    [30, 13, 0],
    [700, 3, 2],
    [80, 16, 1],
    [1200, 0, 2]
]

# Labels:
# 0 = Legitimate, 1 = Fraud
y = [0, 0, 1, 0, 1, 0, 1, 0, 1]

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

def predict_fraud(amount, hour, merchant_type):
    prediction = model.predict([[amount, hour, merchant_type]])[0]

    if prediction == 1:
        return "Fraudulent Transaction"
    else:
        return "Legitimate Transaction"
