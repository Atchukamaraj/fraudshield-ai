import pandas as pd
import numpy as np
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import os

# Create dummy data since we need an end-to-end working example
np.random.seed(42)
n_samples = 10000

# Features: amount, time, transaction_type, location
data = pd.DataFrame({
    'amount': np.random.exponential(100, n_samples),
    'time': np.random.randint(0, 24, n_samples),
    'transaction_type': np.random.randint(0, 5, n_samples),
    'location': np.random.randint(0, 50, n_samples)
})

# Generate labels: higher amount and specific locations have higher fraud probability
# Imbalanced: ~5% fraud
prob = 1 / (1 + np.exp(-(data['amount'] * 0.02 + data['location'] * 0.1 - 5)))
data['fraud'] = (np.random.rand(n_samples) < prob).astype(int)

# Ensure at least some fraud cases
if data['fraud'].sum() == 0:
    data.loc[0:20, 'fraud'] = 1

X = data[['amount', 'time', 'transaction_type', 'location']]
y = data['fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Handle class imbalance using scale_pos_weight
pos_weight = (len(y_train) - sum(y_train)) / max(1, sum(y_train))

model = xgb.XGBClassifier(
    scale_pos_weight=pos_weight,
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, 'model.pkl'), 'wb') as f:
    pickle.dump(model, f)
    
with open(os.path.join(script_dir, 'scaler.pkl'), 'wb') as f:
    pickle.dump(scaler, f)
    
print("Saved model.pkl and scaler.pkl")
