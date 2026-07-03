import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Import CSS
sys.path.append(str(Path(__file__).resolve().parent.parent))
from styles import load_css

st.set_page_config(
    page_title="Feature Importance",
    page_icon="📈",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ======================================
# Header
# ======================================

st.markdown("""
<div class="hero">

<h1>📈 Feature Importance</h1>

<p style="font-size:18px;color:#cbd5e1;">
Understand which customer features influence advertisement click prediction.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================
# Sample Feature Importance
# Replace these values with your actual model coefficients later
# ======================================

importance = pd.DataFrame({
    "Feature": [
        "Daily Time Spent on Site",
        "Age",
        "Area Income",
        "Daily Internet Usage",
        "Male"
    ],
    "Coefficient": [
        2.10,
        -1.62,
        1.35,
        2.82,
        -0.42
    ]
})

importance = importance.sort_values(
    by="Coefficient",
    ascending=True
)

# ======================================
# Plot
# ======================================

fig, ax = plt.subplots(figsize=(8,5))

ax.barh(
    importance["Feature"],
    importance["Coefficient"]
)

ax.set_xlabel("Coefficient Value")
ax.set_title("Feature Importance")

st.pyplot(fig)

# ======================================
# Table
# ======================================

st.markdown("## 📋 Feature Coefficients")

st.dataframe(
    importance,
    use_container_width=True,
    hide_index=True
)

# ======================================
# Explanation
# ======================================

st.markdown("""
<div class="glass">

<h2>🧠 Interpretation</h2>

Positive coefficient → increases the probability of clicking the advertisement.

Negative coefficient → decreases the probability of clicking the advertisement.

Higher absolute values indicate a stronger influence on the prediction.

</div>
""", unsafe_allow_html=True)

# ======================================
# Footer
# ======================================

st.success(
    "These values are illustrative. Replace them with the coefficients from your trained Logistic Regression model for final deployment."
)