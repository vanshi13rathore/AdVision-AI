def load_css():
    return """
<style>

/* ===============================
   Google Font
================================== */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* ===============================
   Global
================================== */
html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:
    radial-gradient(circle at top left,#1f1147 0%,#0f172a 35%,#09090f 100%);
}

/* Hide Streamlit Branding */
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
header{
    visibility:hidden;
}

/* Main Container */
.block-container{
    max-width:1350px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ===============================
   Hero Section
================================== */

.hero{
    background:linear-gradient(
        135deg,
        rgba(124,58,237,.18),
        rgba(59,130,246,.12)
    );

    border:1px solid rgba(255,255,255,.08);

    border-radius:28px;

    padding:45px;

    backdrop-filter:blur(18px);

    box-shadow:0 15px 40px rgba(0,0,0,.35);

    margin-bottom:30px;
}

/* ===============================
   Metric Cards
================================== */

.metric{
    background:rgba(255,255,255,.05);

    padding:28px;

    border-radius:22px;

    border:1px solid rgba(255,255,255,.06);

    text-align:center;

    transition:0.35s;

    backdrop-filter:blur(12px);
}

.metric:hover{
    transform:translateY(-8px);

    border-color:#7c3aed;

    box-shadow:0 20px 40px rgba(124,58,237,.25);
}

.metric-title{
    color:#94a3b8;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:700;
    margin-top:10px;
}

/* ===============================
   Glass Card
================================== */

.glass{
    background:rgba(255,255,255,.05);

    border:1px solid rgba(255,255,255,.07);

    border-radius:24px;

    padding:35px;

    backdrop-filter:blur(14px);

    margin-top:25px;
}

/* ===============================
   Prediction Result Card
================================== */

.result-card{

    background:linear-gradient(
        135deg,
        rgba(34,197,94,.18),
        rgba(59,130,246,.15)
    );

    border-radius:24px;

    padding:35px;

    margin-top:25px;

    border:1px solid rgba(255,255,255,.08);

    backdrop-filter:blur(18px);

    box-shadow:0 20px 50px rgba(0,0,0,.30);
}

.result-title{

    color:white;

    font-size:34px;

    font-weight:700;

    text-align:center;
}

.result-prob{

    color:#38bdf8;

    font-size:60px;

    font-weight:700;

    text-align:center;

    margin-top:15px;
}

.result-text{

    color:#cbd5e1;

    text-align:center;

    font-size:18px;
}

/* ===============================
   Buttons
================================== */

.stButton > button{

    width:100%;

    background:linear-gradient(
        90deg,
        #7c3aed,
        #2563eb
    );

    color:white;

    border:none;

    border-radius:14px;

    padding:14px;

    font-size:17px;

    font-weight:600;

    transition:.3s;
}

.stButton > button:hover{

    transform:scale(1.03);

    box-shadow:0 0 20px rgba(124,58,237,.45);
}

/* ===============================
   Sidebar
================================== */

section[data-testid="stSidebar"]{
    background:#0b1020;
}

/* ===============================
   Divider
================================== */

hr{
    border:none;

    height:1px;

    background:#2d3748;

    margin:30px 0;
}

/* ===========================================
   CUSTOM SCROLLBAR
=========================================== */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-track{
    background:#0f172a;
}

::-webkit-scrollbar-thumb{
    background:#7c3aed;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#8b5cf6;
}

/* ===========================================
   TABLE DESIGN
=========================================== */

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#1e293b;
    color:white;
    padding:12px;
    text-align:left;
}

td{
    padding:12px;
    border-bottom:1px solid rgba(255,255,255,.08);
}

/* ===========================================
   SUCCESS / INFO BOXES
=========================================== */

.stSuccess{
    border-radius:18px;
}

.stInfo{
    border-radius:18px;
}

.stWarning{
    border-radius:18px;
}

.stError{
    border-radius:18px;
}

/* ===========================================
   SLIDERS
=========================================== */

.stSlider{
    padding-top:15px;
    padding-bottom:15px;
}

/* ===========================================
   INPUT BOXES
=========================================== */

.stNumberInput input{
    border-radius:12px;
}

.stSelectbox{
    border-radius:12px;
}

/* ===========================================
   ANIMATION
=========================================== */

.hero,
.metric,
.glass,
.result-card{

animation:fadeUp .6s ease;

}

@keyframes fadeUp{

from{

opacity:0;

transform:translateY(18px);

}

to{

opacity:1;

transform:translateY(0);

}

}

</style>
"""
