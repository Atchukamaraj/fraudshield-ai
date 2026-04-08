# 🛡️ FraudShield AI

### Context-Aware Financial Fraud Detection System

FraudShield AI is an end-to-end **machine learning-based fraud detection system** designed to identify fraudulent financial transactions in real-time. The system uses advanced ML techniques like **XGBoost with cost-sensitive learning** to handle imbalanced datasets and improve detection accuracy.

---

## 🚀 Features

* 🔍 Real-time fraud detection
* ⚖️ Handles imbalanced datasets using cost-sensitive learning
* 🧠 Feature engineering and scaling
* 📊 Risk scoring system (LOW / MEDIUM / HIGH)
* ⚡ FastAPI backend for prediction API
* 🎨 Streamlit frontend for user interaction
* 🌐 Deployment-ready architecture (Render + Streamlit Cloud)
* 🔐 CORS enabled and error handling

---

## 🧱 Project Structure

```
fraudshield-ai/
│
├── backend/
│   └── main.py            # FastAPI backend
│
├── frontend/
│   └── app.py             # Streamlit UI
│
├── model/
│   ├── train.py           # Model training script
│   ├── model.pkl          # Trained model (generated)
│   └── scaler.pkl         # Scaler (generated)
│
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Feature Scaling
5. Handling Imbalanced Data
6. Cost-Sensitive Learning
7. Model Training using XGBoost
8. Model Evaluation
9. Prediction & Risk Classification

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Atchukamaraj/fraudshield-ai.git
cd fraudshield-ai
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Train the Model

```
python model/train.py
```

---

### 4. Run Backend (FastAPI)

```
uvicorn backend.main:app --reload --port 8000
```

👉 Open in browser:
http://127.0.0.1:8000/docs

---

### 5. Run Frontend (Streamlit)

```
streamlit run frontend/app.py
```

---

## 🔌 API Endpoint

### POST `/predict`

### Input:

```
{
  "amount": 5000,
  "time": 14,
  "transaction_type": 2,
  "location": 10
}
```

### Output:

```
{
  "fraud": 1,
  "probability": 0.87,
  "risk_level": "HIGH"
}
```

---

## ⚠️ Risk Classification Logic

| Probability Range | Risk Level |
| ----------------- | ---------- |
| < 0.3             | LOW        |
| 0.3 – 0.7         | MEDIUM     |
| > 0.7             | HIGH       |

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall (important for fraud detection)
* F1 Score
* ROC-AUC

---

## 🌍 Deployment

### Backend (Render)

```
uvicorn backend.main:app --host 0.0.0.0 --port 10000
```

---

### Frontend (Streamlit Cloud)

Set environment variable:

```
BACKEND_URL=https://your-backend-url.onrender.com
```

---

## 🔥 Future Improvements

* Explainable AI using SHAP
* Real-time streaming data
* Advanced analytics dashboard
* Multi-model ensemble approach

---

## 👨💻 Author

**Atchukamaraj**

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
