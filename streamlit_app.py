import streamlit as st

st.set_page_config(
    page_title="Strava Activities Dashboard",
    page_icon="🏃",
    layout="wide",
)

st.title("🏃 Strava Activities Dashboard")
st.markdown("Upload your Strava activities CSV file to analyze your fitness data")

st.sidebar.header("📁 Upload Your Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload your Strava activities CSV file",
    type=['csv'],
)

if uploaded_file is not None:
    st.success("File uploaded! Processing...")
    import pandas as pd
    try:
        df = pd.read_csv(uploaded_file)
        st.write(f"Loaded {len(df)} activities")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("👈 Please upload a Strava activities CSV file using the sidebar")
