import streamlit as st
from pathlib import Path
import sys

# Import custom CSS
sys.path.append(str(Path(__file__).resolve().parent.parent))
from styles import load_css
from utils import predict_customer
from report_generator import generate_report

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)




# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">

<h1>🎯 AI Advertisement Click Prediction</h1>

<p style="font-size:18px;color:#cbd5e1;">
Predict whether a customer is likely to click an online advertisement
using a trained Machine Learning model.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# Customer Information
# =====================================================

st.markdown("## 👤 Customer Information")

col1, col2 = st.columns(2)

with col1:

    time_site = st.slider(
        "Daily Time Spent on Site (minutes)",
        min_value=30.0,
        max_value=100.0,
        value=65.0,
        step=0.1
    )

    age = st.slider(
        "Age",
        min_value=18,
        max_value=65,
        value=35
    )

    income = st.number_input(
        "Area Income ($)",
        min_value=10000.0,
        max_value=100000.0,
        value=55000.0,
        step=500.0
    )

with col2:

    internet = st.slider(
        "Daily Internet Usage (minutes)",
        min_value=100.0,
        max_value=300.0,
        value=180.0,
        step=0.1
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

male = 1 if gender == "Male" else 0

st.write("")

predict = st.button(
    "🚀 Predict Advertisement Click",
    use_container_width=True
)

# =====================================================
# Prediction Logic
# =====================================================

if predict:

    prediction, probability = predict_customer(
        time_site,
        age,
        income,
        internet,
        male
    )

    st.divider()

    st.subheader("🎯 AI Prediction Result")

    st.metric(
        label="Click Probability",
        value=f"{probability * 100:.2f}%"
    )

    st.progress(float(probability))

    # ----------------------------
    # Prediction Status
    # ----------------------------

    if prediction == 1:

        st.success("🟢 HIGH CONVERSION POSSIBILITY")

        st.info("""
### 💼 Business Recommendation

This customer has a **high probability** of clicking the advertisement.

**Recommended Strategy**

- 🎯 Personalized Advertisements
- 💎 Premium Product Campaigns
- 🔄 Retarget Existing Customers
- 📧 Email Marketing
""")

    else:

        st.error("🔴 LOW CONVERSION POSSIBILITY")

        st.warning("""
### 💡 Business Recommendation

This customer has a **low probability** of clicking the advertisement.

**Recommended Strategy**

- 🏷 Discount Campaigns
- 📱 Social Media Marketing
- 🎁 Promotional Offers
- 📢 Brand Awareness Campaigns
""")

    # ----------------------------
    # Download PDF Report
    # ----------------------------

    st.write("")

    pdf_filename = "AdVision_AI_Report.pdf"

    try:

        generate_report(
            pdf_filename,
            time_site,
            age,
            income,
            internet,
            gender,
            prediction,
            probability
        )

        with open(pdf_filename, "rb") as pdf_file:

            st.download_button(
                label="📄 Download Prediction Report",
                data=pdf_file,
                file_name="AdVision_AI_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as e:

        st.error(f"PDF Error: {e}")