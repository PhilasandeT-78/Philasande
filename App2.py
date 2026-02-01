import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Data Analyst Profile",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to:",
    ["Data Analyst Profile", "Education", "Work Experience & Projects", "Contact"]
)

# ---------------------------------------------------
# Data Analyst Profile Section
# ---------------------------------------------------

if menu == "Data Analyst Profile":

    st.title("Data Analyst Profile")

    name = "Khethiwe Ntshangase"
    field = "Mathematics and Physics"
    institution = "Cape Peninsula University of Technology"

    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.image(
        "https://th.bing.com/th/id/OIP.LxP1qwPjHE1CDFmLBh3bxQHaDu",
        caption="Nature (Pixabay)"
    )

# ---------------------------------------------------
# Education Section
# ---------------------------------------------------

elif menu == "Education":

    st.title("Education")

    # -----------------------------
    # Advanced Diploma
    # -----------------------------

    st.subheader("Advanced Diploma in Mathematical Sciences (NQF 7)")
    st.write("**Institution:** Cape Peninsula University of Technology")
    st.write("**Status:** Completed — December 2025")

    st.markdown("### Coursework")
    st.markdown("""
    - Mathematical Statistics  
    - Statistics  
    - Machine Learning and Data Science  
    - Econometrics  
    - Financial Mathematics  
    - Finance  
    - Time Series Forecasting  
    - Numerical Methods  
    - Programming  
    """)

    st.markdown("### Tools")
    st.markdown("""
    - SAS  
    - R  
    - Python  
    - SQL  
    - Microsoft Office  
    - Power BI  
    """)

    st.divider()

    # -----------------------------
    # Postgraduate Diploma
    # -----------------------------

    st.subheader("Postgraduate Diploma in Mathematical Science (NQF 8)")
    st.write("**Status:** Currently Pursuing")

    st.markdown("### Coursework")
    st.markdown("""
    - Bayesian Statistics  
    - Advanced Programming for Data Science  
    - Convex Optimisation  
    - Machine Learning 5A & 5B  
    - Data Engineering and Visualization  
    - Mathematical Modelling  
    - Computational Methods  
    - Research Project  
    """)

    st.markdown("### Tools")
    st.markdown("""
    - SAS  
    - R  
    - Python  
    - SQL  
    - Microsoft Office  
    - Power BI  
    - Tableau  
    """)

# ---------------------------------------------------
# Work Experience & Projects Section
# ---------------------------------------------------

elif menu == "Work Experience & Projects":

    st.title("Work Experience & Projects")

    # -----------------------------
    # Work Experience
    # -----------------------------

    st.subheader("Data Analyst Intern")
    st.write("**Organization:** Statistics South Africa (Stats SA)")
    st.write("**Duration:** July 2024 – December 2024")

    st.markdown("""
    **Responsibilities & Achievements:**
    - Cleaned, validated, and prepared large survey datasets using R, ensuring data integrity and accuracy.  
    - Performed statistical summaries and exploratory analysis to identify trends and data quality issues.  
    - Produced tables, charts, and analytical reports for internal stakeholders.  
    - Investigated data inconsistencies, tested statistical assumptions, and verified outputs.  
    - Collaborated with senior statisticians during reporting cycles and data verification processes.  
    - Gained professional exposure to SAS, SPSS, and Python in a production analytics environment.  
    """)

    st.divider()

    # -----------------------------
    # Projects
    # -----------------------------

    st.subheader("Projects")

    st.markdown("### Impact of Socio-Economic Factors on Education Outcomes (R)")
    st.markdown("""
    - Analysed large-scale survey datasets using R for data cleaning, preprocessing, and exploratory analysis.  
    - Applied multinomial logistic regression to model relationships and predict education outcomes.  
    - Summarised findings through clear reporting and data visualisations.  
    """)

    st.markdown("### Data Analytics on Student Debt (R & Power BI)")
    st.markdown("""
    - Processed demographic and financial datasets using R.  
    - Conducted multiple linear regression for predictive analysis.  
    - Designed interactive Power BI dashboards to visualise trends and key insights.  
    """)

# ---------------------------------------------------
# Contact Section
# ---------------------------------------------------

elif menu == "Contact":

    st.title("Contact Information")

    email = "khethiwentshangase22@gmail.com"

    st.write("You can reach me at:")
    st.write(f"📧 {email}")





