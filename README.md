# 🔥 ML Fraud Detection System

An end-to-end machine learning project for detecting fraudulent transactions, featuring an XGBoost model, a FastAPI backend, and a Streamlit frontend.

## 📁 Project Structure
```
fraudshield-ai/
├── backend/
│   └── main.py       # FastAPI application serving ML predictions
├── frontend/
│   └── app.py        # Streamlit dashboard
├── model/
│   ├── train.py      # Model training script
│   ├── model.pkl     # Generated XGBoost model
│   └── scaler.pkl    # Generated StandardScaler
├── requirements.txt  # Python environment dependencies
└── README.md         # Project documentation
```

## 🚀 Setup Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   cd fraudshield-ai
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate 
   # On Windows:
   venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Generate the model files by running the training script:
   ```bash
   python model/train.py
   ```
   *(This will create `model.pkl` and `scaler.pkl` inside the `model/` folder).*

## 💻 How to Run Locally

### 1. Start the Backend (FastAPI)
Run the backend server on port 8000:
```bash
uvicorn backend.main:app --reload --port 8000
```
- API Documentation (Swagger UI) is available at: http://localhost:8000/docs

### 2. Start the Frontend (Streamlit)
Open a **new terminal window**, activate your virtual environment again, and run:
```bash
streamlit run frontend/app.py
```
- The Streamlit interface will open in your browser typically at http://localhost:8501.

## 🌍 Deployment Steps

### Deploying the Backend to Render

1. Commit and push your code to a GitHub repository.
2. Sign up / Log in to [Render](https://render.com/).
3. Click "New" and select **Web Service**.
4. Connect the GitHub repository you created.
5. Setup the deployment settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
6. Click deploy. Once live, copy the assigned `.onrender.com` URL.

### Deploying the Frontend to Streamlit Cloud

1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Click **New app** and connect your GitHub repository.
3. Configure the app:
   - **Main file path:** `frontend/app.py`
4. Update the Backend connection:
   - To link to your new Render backend, open **Advanced Settings** -> **Secrets** and add:
     ```toml
     BACKEND_URL="https://your-backend-app-name.onrender.com"
     ```
     *(Alternatively, you can manually update the `BACKEND_URL` variable in `frontend/app.py` directly).*
5. Click **Deploy**. The frontend will now securely communicate with your deployed backend!
