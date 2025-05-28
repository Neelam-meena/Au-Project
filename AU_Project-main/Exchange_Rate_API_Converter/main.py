import streamlit as st
from exchange_api import exchange_rate

# Page config
st.set_page_config(page_title="Currency to INR Converter", page_icon="💱", layout="centered")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #2c3e50;'>💱 Currency to INR Converter</h1>
    <p style='text-align: center;'>Select any currency and get real-time conversion rate to INR</p>
""", unsafe_allow_html=True)

# Currency selection
currency_options = ["USD", "AED", "CAD", "EUR", "GBP", "AUD", "SGD", "JPY", "IMP"]
selected_curr = st.selectbox("Choose a currency:", currency_options)

# Button and conversion
if st.button("💹 Convert to INR"):
    INR_VAL = exchange_rate(selected_curr)
    if INR_VAL:
        st.success(f"✅ 1 {selected_curr} = ₹ {INR_VAL}")
    else:
        st.error("❌ Could not fetch data. Please try again later.")