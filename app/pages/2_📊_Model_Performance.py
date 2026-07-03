import streamlit as st
from pathlib import Path
import sys

# Import CSS
sys.path.append(str(Path(__file__).resolve().parent.parent))
from styles import load_css

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ============================
# Header
# ============================

st.markdown("""
<div class="hero">

<h1>📊 Model Performance Dashboard</h1>

<p style="font-size:18px;color:#cbd5e1;">
Performance evaluation of the Logistic Regression model used for advertisement click prediction.
</p>

</div>
""", unsafe_allow_html=True)

# ============================
# Metrics
# ============================

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("🎯 Accuracy", "96%"),
    ("📌 Precision", "95%"),
    ("🔄 Recall", "96%"),
    ("⚖️ F1 Score", "95%")
]

for col, (title, value) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ============================
# Model Information
# ============================

st.markdown("""
<div class="glass">

<h2>🤖 Model Details</h2>

| Property | Value |
|-----------|-------|
| Algorithm | Logistic Regression |
| Problem Type | Binary Classification |
| Dataset | Advertisement.csv |
| Training Records | 1000 |
| Input Features | 5 |
| Target Variable | Clicked on Ad |

</div>
""", unsafe_allow_html=True)

st.write("")

# ============================
# Feature Summary
# ============================

st.markdown("""
<div class="glass">

<h2>📋 Features Used</h2>

- Daily Time Spent on Site
- Age
- Area Income
- Daily Internet Usage
- Gender (Male)

</div>
""", unsafe_allow_html=True)

st.write("")

# ============================
# Confusion Matrix
# ============================

st.markdown("""
<div class="glass">

<h2>📉 Sample Confusion Matrix</h2>

| | Predicted No | Predicted Yes |
|---|---:|---:|
| Actual No | 95 | 4 |
| Actual Yes | 3 | 98 |

</div>
""", unsafe_allow_html=True)

st.write("")

# ============================
# Conclusion
# ============================

st.success("""
✅ The Logistic Regression model demonstrates strong classification performance,
making it suitable for predicting advertisement click behaviour.
""")