import streamlit as st
from pathlib import Path
import sys

# Import CSS
sys.path.append(str(Path(__file__).resolve().parent.parent))
from styles import load_css

st.set_page_config(
    page_title="About Developer",
    page_icon="👩‍💻",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.markdown("""
<div class="hero">

<h1>👩‍💻 About the Developer</h1>

<p style="font-size:18px;color:#cbd5e1;">
Meet the developer behind AdVision-AI.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# Profile
# ==========================

left, right = st.columns([1,2])

with left:
    st.markdown("""
<div class="glass">

## 👩‍🎓 Vanshika Rathore

🎓 B.Tech CSE (AI & ML)

📍 India

</div>
""", unsafe_allow_html=True)

with right:
    st.markdown("""
<div class="glass">

## 🚀 Career Objective

Aspiring AI Engineer passionate about Machine Learning,
Artificial Intelligence and Data Science.

Interested in building intelligent systems that solve
real-world business problems.

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# Skills
# ==========================

st.markdown("""
<div class="glass">

<h2>🛠 Technical Skills</h2>

✅ Python

✅ SQL

✅ Machine Learning

✅ Data Analysis

✅ Scikit-learn

✅ Streamlit

✅ Pandas

✅ NumPy

✅ Git & GitHub

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# Project Tech Stack
# ==========================

st.markdown("""
<div class="glass">

<h2>⚙ Technologies Used in AdVision-AI</h2>

• Python

• Pandas

• NumPy

• Scikit-learn

• Logistic Regression

• Joblib

• Streamlit

• Matplotlib

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# Contact
# ==========================

st.markdown("""
<div class="glass">

<h2>📬 Connect With Me</h2>

📧 Email:
your-rathorevanshika460@gmail.com

💻 GitHub:
https://github.com/vanshi13rathore

🔗 LinkedIn:
https://www.linkedin.com/in/vanshika-rathore-37672728b/


</div>
""", unsafe_allow_html=True)

st.write("")

st.success(
    "Thank you for visiting AdVision-AI!"
)