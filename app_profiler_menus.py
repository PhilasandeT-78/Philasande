import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Philasande Tshusha | Data Analyst Portfolio",
    layout="wide"
)

# -------------------------------------------------
# GLOBAL STYLES (STYLE ONLY)
# -------------------------------------------------
st.markdown(f"""
<style>

/* -------------------------------------------------
   BASE (LIGHT MODE)
--------------------------------------------------*/

html, body, [class*="css"] {{
    font-family: "Segoe UI", sans-serif;
    background-color: #ffffff;
    color: #000000;
}}

.profile-title {{
    font-size: 38px;
    font-weight: 700;
    color: #0b5fff;
}}

.profile-sub {{
    font-size: 16px;
    color: #444;
    margin-bottom: 12px;
}}

.card {{
    background-color: #f8f9ff;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    margin-bottom: 20px;
    animation: slideUp 0.6s ease forwards;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}}

.card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}}

img {{
    border-radius: 18px;
    transition: transform 0.25s ease;
}}
img:hover {{
    transform: scale(1.03);
}}

.stButton > button {{
    background-color: #0b5fff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    transition: background-color 0.25s ease, transform 0.2s ease;
}}
.stButton > button:hover {{
    background-color: #0846cc;
    transform: translateY(-2px);
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #0b5fff, #4f8cff);
}}
section[data-testid="stSidebar"] * {{
    color: white !important;
}}

/* -------------------------------------------------
   DARK MODE
--------------------------------------------------*/

{"body, .main { background-color: #0e1117; color: #e6e6e6; }" if dark_mode else ""}

{"h1, h2, h3, h4 { color: #9dbbff; }" if dark_mode else ""}

{".profile-sub { color: #b0b0b0; }" if dark_mode else ""}

{".card { background-color: #1c1f26; box-shadow: 0 10px 30px rgba(0,0,0,0.6); }" if dark_mode else ""}

{".stButton > button { background-color: #4f8cff; }" if dark_mode else ""}

{".stButton > button:hover { background-color: #6b9cff; }" if dark_mode else ""}

{"""
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0d14, #151922);
}
""" if dark_mode else ""}

/* -------------------------------------------------
   ANIMATIONS
--------------------------------------------------*/

@keyframes slideUp {{
    from {{
        opacity: 0;
        transform: translateY(18px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.main {{
    animation: fadeIn 0.6s ease-in;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; }}
    to {{ opacity: 1; }}
}}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Skills", "Experience", "Projects", "Education", "Contact"]
)

# -------------------------------------------------
# HOME
# -------------------------------------------------
if menu == "Home":

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown('<div class="profile-title">Philasande Tshusha</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="profile-sub">Junior Data Analyst | Mathematical Science | Python, SQL, Power BI</div>',
            unsafe_allow_html=True
        )

        st.write(
            """
            Detail-oriented Junior Data Analyst with a strong foundation in applied mathematical sciences,
            statistical analysis, and data management. Experienced in dashboard development, survey data
            analysis, and predictive modeling to support data-driven decision-making.
            """
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.image(
            "https://media.licdn.com/dms/image/v2/D4D35AQG6X6LSjA1GwQ/profile-framedphoto-shrink_400_400/B4DZX3nnFdGwAc-/0/1743616111229?e=1770577200&v=beta&t=w0Pxo8-H_thPr4qyn7HNh66yvcifjzJKL7g-4gQWH4w",
            width=300
        )

    st.divider()

# -------------------------------------------------
# ABOUT
# -------------------------------------------------
elif menu == "About":

    st.header("About Me")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write(
        """
        I am a Mathematical Science graduate with strong foundations in statistics,
        numerical methods, and computational problem-solving.

        My work focuses on transforming raw data into actionable insights through:
        """
    )

    st.write("""
    - Statistical analysis and modeling  
    - Survey design and data quality assurance  
    - Dashboard development and reporting  
    - Data-driven decision support  
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Qualification", "Advanced Diploma")
    col2.metric("Field", "Mathematical Science")
    col3.metric("Industry Experience", "Public Sector")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# SKILLS
# -------------------------------------------------
elif menu == "Skills":

    st.header("Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Core Data Skills")
        st.write("""
        - Python (Pandas, NumPy, Flask)
        - SQL (SQLite, database queries)
        - Power BI (Dashboards & reporting)
        - R (Statistical analysis)
        - SAS
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Mathematical & Analytical Skills")
        st.write("""
        - Mathematical Statistics
        - Numerical Methods
        - Machine Learning (coursework)
        - Differential Equations
        - Optimization Techniques
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# EXPERIENCE
# -------------------------------------------------
elif menu == "Experience":

    st.header("Work Experience")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Junior Data Analyst — Cape Peninsula University of Technology")
    st.caption("June 2025 – Present")
    st.write("""
    - Develop dashboards for internal and external reporting  
    - Support teams in designing and refining surveys  
    - Apply predictive methods using machine learning techniques  
    - Contribute to student success initiatives through data-driven insights  
    """)

    st.divider()

    st.subheader("Data Analyst Intern — Statistics South Africa")
    st.caption("July 2024 – December 2024")
    st.write("""
    - Designed and developed a data collection website for agricultural data  
    - Assisted with data quality monitoring to ensure accurate reporting  
    - Processed and analyzed datasets using R and Python  
    - Gained practical exposure to HTML, CSS, SQLite, and Python  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# PROJECTS
# -------------------------------------------------
elif menu == "Projects":

    st.header("Projects")

    with st.expander("📊 Zika Virus Mathematical Model"):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("""
        In this paper we discuss Zika virus, a mosquito-borne virus first identified in Uganda and
        currently dominant in tropical and subtropical regions. We devise and analyze a model
        that accounts for both vector and sexual transmission, and we investigate the effects of
        human awareness and vector control (excluding disease-caused mortality). We derive the
        disease-free and endemic equilibrium points and show the disease-free equilibrium is
        locally stable when R0 < 1 while the endemic equilibrium is locally stable when R0 > 1.
        We perform a partial rank correlation coefficient analysis for the basic reproduction number
        to identify parameters that increase R0, and we conduct sensitivity analyses by running
        simulations in MATLAB (Euler's method) while varying key parameters. Our results
        highlight which control measures are most effective at slowing the spread of the virus.
        """)
        st.write("**Tools:** MATLAB, Differential Equations, Numerical Simulation")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🌱 Agriculture Data Collection Platform"):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("""
        This research developed and implemented a user-friendly web-based data collection
        platform to improve data collection for the agricultural sector of Statistics South
        Africa (Stats SA). The current pen-and-paper method is inefficient, costly, time-consuming,
        and prone to human error; an online survey platform provides a more efficient,
        cost-effective, and scalable alternative. The front end was built with HTML, CSS, and
        JavaScript while the backend uses Flask (Python) and SQLAlchemy for data storage.
        A pilot study with 17 participants from the Western Cape Stats SA office reported an
        82% completion rate and reduced data collection time. Key features include real-time
        data validation, improved accuracy, enhanced data security, a built-in chatbot, and
        scalability. Despite limitations such as no email validation in the pilot, the platform
        demonstrates strong potential to simplify and scale agricultural data collection for
        Stats SA.
        """)
        st.write("**Tools:** Python, Flask, SQLAlchemy, HTML/CSS/JavaScript")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🦟 Dengue Fever Modeling"):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("""
        Dengue fever is a mosquito-borne illness caused by four antigenically distinct viruses
        (DENV-1 to DENV-4). To study transmission dynamics we adapt compartmental models
        (e.g., SIR/SIRS) to include vector transmission, population immunity, and mosquito
        population dynamics. In our analysis we estimated a basic reproduction number R0 = 4.021
        (> 1), indicating endemic transmission under baseline assumptions. We ran simulations
        in MATLAB for the SIRS model to evaluate future incidence and intervention scenarios,
        demonstrating the model's utility for forecasting and planning control measures.
        """)
        st.write("**Tools:** MATLAB, R, Compartmental Modeling")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# EDUCATION
# -------------------------------------------------
elif menu == "Education":

    st.header("Education")

    st.markdown("""
    <div class="card">
    <h3>Postgraduate Diploma in Mathematical Science (NQF 8)</h3>
    <b>Status:</b> Currently Pursuing

    <h4>Coursework</h4>
    <ul>
        <li>Bayesian Statistics</li>
        <li>Advanced Programming for Data Science</li>
        <li>Convex Optimisation</li>
        <li>Machine Learning 5A & 5B</li>
        <li>Data Engineering & Visualisation</li>
    </ul>

    <h4>Tools</h4>
    SAS · R · Python · SQL · Power BI · Tableau
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Advanced Diploma in Mathematical Science")
    st.caption("Cape Peninsula University of Technology | 2025")
    st.write("""
    Relevant Coursework:
    - Machine Learning & Data Science
    - Mathematical Statistics
    - Numerical Methods
    - Mathematical Analysis
    - Biostatistics
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Diploma in Mathematical Science")
    st.caption("Cape Peninsula University of Technology | 2022 – 2024")
    st.write("""
    - Programming (Python, R, SAS)
    - Data Management
    - Operations Research
    - Biomathematics
    - Mathematical Science Project
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# CONTACT
# -------------------------------------------------
elif menu == "Contact":

    st.header("Contact Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("📧 **Email:** philasandetshusha1@gmail.com")
        st.write("📞 **Phone:** +27 78 643 9409")
        st.write("📍 **Location:** South Africa")
        st.markdown(
            "[LinkedIn Profile](https://www.linkedin.com/in/philasande-tshutsha-7434a026b)"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Send a Message")

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")

        if st.button("Send"):
            st.success("Thank you! Your message has been sent.")

        st.markdown('</div>', unsafe_allow_html=True)





