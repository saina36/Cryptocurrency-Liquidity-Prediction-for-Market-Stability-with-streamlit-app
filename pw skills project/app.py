import streamlit as st
import joblib
import numpy as np

# Load model and assets
model = joblib.load("gradient_boost_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")  # ['volume_to_market_cap', '1h', '24h', '7d']

# Liquidity classification logic
def classify_liquidity(ratio):
    if ratio < 0.05:
        return "Low"
    elif ratio < 0.15:
        return "Medium"
    else:
        return "High"

# App UI
st.title("🪙 Cryptocurrency Liquidity Predictor")
st.write("Enter market data to predict liquidity ratio and classify market stability.")

# User Inputs
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        one_h = st.number_input("1h % change", value=0.01)
        volume = st.number_input("24h Volume (USD)", value=1e7)

    with col2:
        twenty_four_h = st.number_input("24h % change", value=0.02)
        seven_d = st.number_input("7d % change", value=0.05)

    # ✅ Full-width Market Cap input aligned below both columns
    market_cap = st.number_input("Market Cap (USD)", value=5e8)

    submitted = st.form_submit_button("Predict Liquidity")

if submitted:
    try:
        # Feature Engineering
        volume_to_market_cap = volume / market_cap if market_cap != 0 else 0

        # Prepare final input for model
        input_data = np.array([[volume_to_market_cap, one_h, twenty_four_h, seven_d]])
        input_scaled = scaler.transform(input_data)

        # Prediction
        pred_ratio = model.predict(input_scaled)[0]
        pred_class = classify_liquidity(pred_ratio)

        # Display results
        st.success(f"💧 **Predicted Liquidity Ratio:** {pred_ratio:.5f}")
        st.info(f"🔍 **Liquidity Classification:** {pred_class}")

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
