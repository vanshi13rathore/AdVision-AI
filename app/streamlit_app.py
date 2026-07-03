import streamlit as st
from styles import load_css

st.set_page_config(
    page_title="AdVision-AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>🧠 AdVision-AI</h1>

<h2>AI-Powered Advertisement Click Prediction</h2>

<p style="font-size:20px;color:#cbd5e1;">

Predict customer behaviour before launching digital marketing campaigns using Machine Learning.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- METRICS ---------------- #

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("🎯 Accuracy", "96%"),
    ("🤖 Algorithm", "Logistic Regression"),
    ("📊 Dataset", "1000 Records"),
    ("📈 Features", "5")
]

for col, (title, value) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(f"""
        <div class="metric">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ---------------- ABOUT ---------------- #

st.markdown("""
<div class="glass">

<h2>📖 About This Project</h2>

AdVision-AI is an end-to-end Machine Learning application that predicts whether a customer is likely to click an online advertisement.

The project demonstrates the complete ML workflow from data preprocessing to deployment.

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- TECHNOLOGIES ---------------- #

st.markdown("""
<div class="glass">

<h2>🛠️ Technology Stack</h2>

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Streamlit | Web Application |
| Joblib | Model Serialization |

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- WORKFLOW ---------------- #

st.markdown("""
<div class="glass">

<h2>⚙️ Machine Learning Workflow</h2>

✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Feature Engineering

✅ Feature Scaling

✅ Logistic Regression Training

✅ Model Evaluation

✅ Web Deployment

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- HOW TO USE ---------------- #

st.markdown("""
<div class="glass">

<h2>🚀 How to Use</h2>

1. Open the **Prediction** page from the sidebar.
2. Enter customer information.
3. Click **Predict Advertisement Click**.
4. View prediction probability.
5. Read the business recommendation.

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>

<center>

<h4>Developed by Vanshika Rathore</h4>

AI • Machine Learning • Streamlit

</center>
""", unsafe_allow_html=True)