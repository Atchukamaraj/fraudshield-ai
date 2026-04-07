import streamlit as st
import requests
import os

# Deployment-ready: Use environment variable, fallback to localhost for development
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
# Remove trailing slash to prevent URL resolution issues during requests
BACKEND_URL = BACKEND_URL.rstrip("/")

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🛡️ ML Fraud Detection System")

st.markdown("### Transaction Details")
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Amount ($)", min_value=0.0, value=120.50, step=10.0)
    time = st.number_input("Time (Hour of day 0-23)", min_value=0, max_value=23, value=14)
with col2:
    transaction_type = st.number_input("Transaction Type (0-4)", min_value=0, max_value=4, value=2)
    location = st.number_input("Location ID (0-50)", min_value=0, max_value=50, value=15)

if st.button("Evaluate Transaction"):
    payload = {
        "amount": amount,
        "time": time,
        "transaction_type": transaction_type,
        "location": location
    }
    
    with st.spinner("Analyzing transaction..."):
        try:
            # Ensure the API call uses the environment variable logic securely
            response = requests.post(f"{BACKEND_URL}/predict", json=payload)
            response.raise_for_status()
            result = response.json()
            
            if "error" in result:
                st.error(result["error"])
            else:
                prob = result['probability']
                risk = result['risk_level']
                
                if risk == "LOW":
                    color = "#28a745" # Green
                elif risk == "MEDIUM":
                    color = "#ffc107" # Yellow
                else:
                    color = "#dc3545" # Red
                    
                st.markdown(f"<h2 style='text-align: center; color: {color};'>Risk Level: {risk}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center;'>Fraud Probability: <strong>{prob:.2%}</strong></p>", unsafe_allow_html=True)
                
                if result['fraud'] == 1:
                    st.error("🚨 ALERT: High probability of fraud detected! Block transaction.")
                else:
                    st.success("✅ Transaction verified. Normal activity.")
                
        except requests.exceptions.ConnectionError:
            st.error(f"Failed to connect to backend at {BACKEND_URL}. Ensure it is running.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
