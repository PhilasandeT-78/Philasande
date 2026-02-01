import streamlit as st
import pandas as pd

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
    ["Data Analyst Profile", "Publications", "STEM Data Explorer", "Contact"]
)

# ---------------------------------------------------
# Dummy STEM Data
# ---------------------------------------------------

physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5)
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5)
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5)
})

# ---------------------------------------------------
# Data Analyst Profile Section
# ---------------------------------------------------

if menu == "Data Analyst Profile":

    st.title("Data Analyst Profile")
    st.sidebar.header("Profile Options")

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
# Publications Section
# ---------------------------------------------------

elif menu == "Publications":

    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    uploaded_file = st.file_uploader(
        "Upload a CSV of Publications",
        type="csv"
    )

    if uploaded_file:

        publications = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Publications")
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword")

        if keyword:

            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]

            st.subheader("Filtered Results")
            st.dataframe(filtered)

        else:
            st.info("Showing all publications")

        if "Year" in publications.columns:

            st.subheader("Publication Trends")

            year_counts = publications["Year"].value_counts().sort_index()

            st.bar_chart(year_counts)

        else:
            st.warning("No 'Year' column found for trend visualization.")

# ---------------------------------------------------
# STEM Data Explorer Section
# ---------------------------------------------------

elif menu == "STEM Data Explorer":

    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")

    data_option = st.sidebar.selectbox(
        "Choose a dataset",
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    # Physics Data
    if data_option == "Physics Experiments":

        st.subheader("Physics Experiment Data")
        st.dataframe(physics_data)

        energy_filter = st.slider(
            "Filter by Energy (MeV)",
            0.0,
            10.0,
            (0.0, 10.0)
        )

        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]

        st.write("Filtered Results")
        st.dataframe(filtered_physics)

    # Astronomy Data
    elif data_option == "Astronomy Observations":

        st.subheader("Astronomy Observation Data")
        st.dataframe(astronomy_data)

        brightness_filter = st.slider(
            "Filter by Brightness (Magnitude)",
            -15.0,
            5.0,
            (-15.0, 5.0)
        )

        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]

        st.write("Filtered Results")
        st.dataframe(filtered_astronomy)

    # Weather Data
    elif data_option == "Weather Data":

        st.subheader("Weather Data")
        st.dataframe(weather_data)

        temp_filter = st.slider(
            "Filter by Temperature (°C)",
            -10.0,
            40.0,
            (-10.0, 40.0)
        )

        humidity_filter = st.slider(
            "Filter by Humidity (%)",
            0,
            100,
            (0, 100)
        )

        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]

        st.write("Filtered Results")
        st.dataframe(filtered_weather)

# ---------------------------------------------------
# Contact Section
# ---------------------------------------------------

elif menu == "Contact":

    st.title("Contact Information")

    email = "khethiwentshangase22@gmail.com"

    st.write("You can reach me at:")
    st.write(f"📧 {email}")


