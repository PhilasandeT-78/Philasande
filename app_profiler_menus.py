import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Philasande Tshusha | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# GLOBAL STYLES
# -------------------------------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(120deg, #0b5fff, #4f8cff);
    padding: 40px;
    border-radius: 18px;
    color: white;
}
.hero h1 { font-size: 48px; margin-bottom: 0; }
.hero p { font-size: 18px; opacity: 0.95; }

.kpi {
    background: #f5f7ff;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
}

.timeline {
    border-left: 3px solid #0b5fff;
    padding-left: 20px;
    margin-left: 5px;
}

.card {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.skill-bar {
    height: 8px;
    background: #e0e6ff;
    border-radius: 5px;
}
.skill-fill {
    height: 8px;
    background: #0b5fff;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "About", "Skills", "Experience", "Projects", "Education", "Contact"]
)

# -------------------------------------------------
# HOME
# -------------------------------------------------
if menu == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Philasande Tshusha</h1>
        <p>Junior Data Analyst • Mathematical Science • Turning Data into Decisions</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)
    col1.markdown('<div class="kpi"><h2>3+</h2><p>Years Study</p></div>', unsafe_allow_html=True)
    col2.markdown('<div class="kpi"><h2>15+</h2><p>Datasets Analyzed</p></div>', unsafe_allow_html=True)
    col3.markdown('<div class="kpi"><h2>5+</h2><p>Dashboards Built</p></div>', unsafe_allow_html=True)
    col4.markdown('<div class="kpi"><h2>2</h2><p>Public Sector Roles</p></div>', unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("👋 Who I Am")
        st.write("""
        I am a **Mathematical Science graduate and Junior Data Analyst** with experience in
        public sector analytics, survey data analysis, dashboard development, and applied modeling.

        I enjoy working at the intersection of **statistics, programming, and decision-making**.
        """)

    with col2:
        st.image(
            "https://media.licdn.com/dms/image/v2/D4D35AQG6X6LSjA1GwQ/profile-framedphoto-shrink_400_400/B4DZX3nnFdGwAc-/0/1743616111229",
            width=260
        )

# -------------------------------------------------
# ABOUT
# -------------------------------------------------
elif menu == "About":

    st.header("About Me")
    st.write("""
    My background in **Mathematical Science** gives me a strong analytical foundation,
    while my practical experience allows me to deliver **real-world data solutions**.
    """)

    st.markdown("""
    **What I focus on:**
    - Translating complex data into clear insights  
    - Ensuring data quality and reliability  
    - Supporting policy and institutional decisions  
    """)

# -------------------------------------------------
# SKILLS
# -------------------------------------------------
elif menu == "Skills":

    st.header("Technical Skills")

    skills = {
        "Python": 90,
        "SQL": 80,
        "Power BI": 85,
        "R": 75,
        "SAS": 70,
        "Statistics": 90
    }

    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.markdown(
            f'<div class="skill-bar"><div class="skill-fill" style="width:{level}%"></div></div>',
            unsafe_allow_html=True
        )

# -------------------------------------------------
# EXPERIENCE
# -------------------------------------------------
elif menu == "Experience":

    st.header("Experience")

    st.markdown("""
    <div class="timeline">
        <h4>Junior Data Analyst — CPUT</h4>
        <p><i>June 2025 – Present</i></p>
        <ul>
            <li>Built dashboards for institutional reporting</li>
            <li>Designed and analyzed surveys</li>
            <li>Applied predictive and ML techniques</li>
        </ul>

        <h4>Data Analyst Intern — Statistics South Africa</h4>
        <p><i>July 2024 – Dec 2024</i></p>
        <ul>
            <li>Developed agricultural data collection system</li>
            <li>Improved data quality monitoring</li>
            <li>Worked with Python, R, SQL, HTML/CSS</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# PROJECTS
# -------------------------------------------------
elif menu == "Projects":

    st.header("Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>🦟 Zika Virus Mathematical Model</h4>
            <p>Compartmental modeling with awareness and control strategies.
            Stability analysis and sensitivity simulations.</p>
            <b>Tools:</b> MATLAB, Numerical Methods
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>🌱 Agriculture Data Collection Platform</h4>
            <p>Web-based survey platform replacing paper-based collection at Stats SA.</p>
            <b>Tools:</b> Python, Flask, SQLAlchemy
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# EDUCATION
# -------------------------------------------------
elif menu == "Education":

    st.header("Education")

    st.markdown("""
    <div class="card">
        <h4>Postgraduate Diploma in Mathematical Science (NQF 8)</h4>
        <p><b>Status:</b> Currently Pursuing</p>
        <p>Bayesian Statistics · Machine Learning · Data Engineering</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# CONTACT
# -------------------------------------------------
elif menu == "Contact":

    st.header("Let’s Connect")

    col1, col2 = st.columns(2)

    with col1:
        st.write("📧 philasandetshusha1@gmail.com")
        st.write("📞 +27 78 643 9409")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/philasande-tshutsha-7434a026b)")

    with col2:
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        st.button("Send Message 🚀")



