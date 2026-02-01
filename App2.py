import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Philasande Tshusha | Data Analyst Portfolio",
    layout="wide"
)

# ---------------------------------------------------
# GLOBAL STYLES
# ---------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #F8F9FC;
    color: #1F2937;
    font-family: "Segoe UI", sans-serif;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 15px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    margin-bottom: 25px;
}

.card:hover {
    box-shadow: 0 12px 28px rgba(0,0,0,0.1);
}

.hero-name {
    font-size: 42px;
    font-weight: 700;
}

.hero-role {
    color: #2563EB;
    font-size: 20px;
    margin-bottom: 10px;
}

.small-text {
    color: #6B7280;
}

img {
    border-radius: 16px;
}

.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    border: none;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: #1D4ED8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.markdown("""
<h2 style="color:#2563EB;">📊 Portfolio</h2>
<p class="small-text">Navigate my profile</p>
""", unsafe_allow_html=True)

st.sidebar.divider()

menu = st.sidebar.radio(
    "Menu",
    ["Home", "About", "Skills", "Experience", "Projects", "Education", "Contact"]
)

# ---------------------------------------------------
# HOME
# ---------------------------------------------------
if menu == "Home":

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="card">
            <div class="hero-name">Philasande Tshusha</div>
            <div class="hero-role">
                Junior Data Analyst | Mathematical Science
            </div>
            <p>
            Detail-oriented Junior Data Analyst with a strong foundation in applied
            mathematical sciences, statistics, and data management.
            Experienced in dashboard development, survey data analysis,
            and predictive modelling to support data-driven decision-making.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://media.licdn.com/dms/image/v2/D4D35AQG6X6LSjA1GwQ/profile-framedphoto-shrink_400_400/B4DZX3nnFdGwAc-/0/1743616111229?e=1770577200&v=beta&t=w0Pxo8-H_thPr4qyn7HNh66yvcifjzJKL7g-4gQWH4w",
            use_column_width=True
        )

# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------
elif menu == "About":

    st.markdown('<div class="section-title">👩🏽‍💻 About Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    I am a Mathematical Science graduate with strong foundations in statistics,
    numerical methods, and computational problem-solving.
    <br><br>
    My work focuses on transforming raw data into actionable insights through
    statistical modelling, dashboard development, and data-driven decision support.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Qualification", "Advanced Diploma")
    col2.metric("Field", "Mathematical Science")
    col3.metric("Industry Experience", "Public Sector")

# ---------------------------------------------------
# SKILLS
# ---------------------------------------------------
elif menu == "Skills":

    st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>Data & Programming</h3>
        <ul>
            <li>Python (Pandas, NumPy, Flask)</li>
            <li>SQL (SQLite)</li>
            <li>Power BI (Dashboards)</li>
            <li>R & SAS</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>Mathematical & Analytical</h3>
        <ul>
            <li>Mathematical Statistics</li>
            <li>Numerical Methods</li>
            <li>Machine Learning (coursework)</li>
            <li>Optimisation Techniques</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------
elif menu == "Experience":

    st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Junior Data Analyst — Cape Peninsula University of Technology</h3>
    <p class="small-text">June 2025 – Present</p>
    <ul>
        <li>Develop dashboards for internal and external reporting</li>
        <li>Support survey design and refinement</li>
        <li>Apply predictive methods and analytics</li>
        <li>Support student success initiatives</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Data Analyst Intern — Statistics South Africa</h3>
    <p class="small-text">July 2024 – December 2024</p>
    <ul>
        <li>Built a data collection website for agricultural surveys</li>
        <li>Performed data quality monitoring and validation</li>
        <li>Processed datasets using R and Python</li>
        <li>Worked with Flask, SQLAlchemy, HTML/CSS</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# PROJECTS
# ---------------------------------------------------
elif menu == "Projects":

    st.markdown('<div class="section-title">📈 Projects</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🦠 Zika Virus Mathematical Model</h3>
    Developed and analysed a mathematical model incorporating vector and sexual transmission.
    Conducted stability analysis and sensitivity simulations using Euler’s method.
    <br><br>
    <b>Tools:</b> MATLAB, Differential Equations
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🌱 Agriculture Data Collection Platform</h3>
    Built a web-based survey platform to replace paper-based data collection at Stats SA.
    Improved efficiency, accuracy, and scalability.
    <br><br>
    <b>Tools:</b> Python, Flask, SQLAlchemy, HTML/CSS/JavaScript
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🦟 Dengue Fever Modelling</h3>
    Adapted compartmental models (SIR/SIRS) to analyse dengue transmission dynamics
    and forecast future incidence.
    <br><br>
    <b>Tools:</b> MATLAB, R
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# EDUCATION
# ---------------------------------------------------
elif menu == "Education":

    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)

    # ---------------------------------------------------
    # Postgraduate Diploma
    # ---------------------------------------------------
    st.markdown("""
    <div class="card">
    <h3>Postgraduate Diploma in Mathematical Science (NQF 8)</h3>
    <p class="small-text"><b>Status:</b> Currently Pursuing</p>

    <h4>Coursework</h4>
    <ul>
        <li>Bayesian Statistics</li>
        <li>Advanced Programming for Data Science</li>
        <li>Convex Optimisation</li>
        <li>Machine Learning 5A & 5B</li>
        <li>Data Engineering & Visualisation</li>
        <li>Mathematical Modelling</li>
        <li>Computational Methods</li>
        <li>Research Project</li>
    </ul>

    <h4>Tools</h4>
    SAS · R · Python · SQL · Power BI · Tableau
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # Advanced Diploma
    # ---------------------------------------------------
    st.markdown("""
    <div class="card">
    <h3>Advanced Diploma in Mathematical Science (NQF 7)</h3>
    <p class="small-text">Cape Peninsula University of Technology · 2025</p>

    <h4>Coursework</h4>
    <ul>
        <li>Machine Learning & Data Science</li>
        <li>Mathematical Statistics</li>
        <li>Numerical Methods</li>
        <li>Mathematical Analysis</li>
        <li>Biostatistics</li>
        <li>Time Series Analysis</li>
        <li>Financial Mathematics</li>
    </ul>

    <h4>Tools</h4>
    Python · R · SAS · SQL · Power BI
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # Diploma
    # ---------------------------------------------------
    st.markdown("""
    <div class="card">
    <h3>Diploma in Mathematical Science</h3>
    <p class="small-text">Cape Peninsula University of Technology · 2022 – 2024</p>

    <h4>Coursework</h4>
    <ul>
        <li>Programming (Python, R, SAS)</li>
        <li>Data Management</li>
        <li>Operations Research</li>
        <li>Biomathematics</li>
        <li>Mathematical Statistics</li>
        <li>Mathematical Science Project</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# CONTACT
# ---------------------------------------------------
elif menu == "Contact":

    st.markdown('<div class="section-title">📬 Contact</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>Get in Touch</h3>
        📧 philasandetshusha1@gmail.com<br>
        📞 +27 78 643 9409<br>
        📍 South Africa
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "🔗 Visit my LinkedIn",
            "https://www.linkedin.com/in/philasande-tshutsha-7434a026b"
        )

    with col2:
        st.markdown("""
        <div class="card">
        <h3>Send a Message</h3>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")

        if st.button("Send"):
            st.success("Thank you! Your message has been sent.")
            
            
            dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)









