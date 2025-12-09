import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Strava Activities Dashboard",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header-title {
        color: #FC5200;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="header-title">🏃 Strava Activities Dashboard</div>', unsafe_allow_html=True)
st.markdown("Analyze your fitness data with interactive charts and insights")

# Sidebar for file upload
st.sidebar.header("📁 Upload Your Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload your Strava activities CSV file",
    type=['csv'],
)

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Data preprocessing
    @st.cache_data
    def preprocess_data(df):
        df_processed = df.copy()
        
        # Convert date columns
        date_cols = [col for col in df_processed.columns if 'date' in col.lower()]
        for col in date_cols:
            try:
                df_processed[col] = pd.to_datetime(df_processed[col])
            except:
                pass
        
        # Convert numeric columns
        numeric_cols = [col for col in df_processed.columns if any(x in col.lower() for x in ['distance', 'elevation', 'calories', 'heart rate', 'hr'])]
        for col in numeric_cols:
            if df_processed[col].dtype == 'object':
                df_processed[col] = pd.to_numeric(df_processed[col].str.replace(',', ''), errors='coerce')
        
        return df_processed
    
    df = preprocess_data(df)
    
    # Get column names
    date_col = next((col for col in df.columns if 'date' in col.lower()), None)
    distance_col = next((col for col in df.columns if 'distance' in col.lower()), None)
    activity_col = next((col for col in df.columns if 'type' in col.lower()), None)
    elevation_col = next((col for col in df.columns if 'elevation' in col.lower()), None)
    calorie_col = next((col for col in df.columns if 'calories' in col.lower()), None)
    hr_col = next((col for col in df.columns if 'avg' in col.lower() and 'heart' in col.lower()), None)
    gear_col = next((col for col in df.columns if 'gear' in col.lower()), None)
    
    # Add day of week
    if date_col:
        df['Day of Week'] = df[date_col].dt.day_name()
    
    # Filters
    st.sidebar.header("🔍 Filters")
    
    df_filtered = df.copy()
    
    if activity_col:
        selected_activities = st.sidebar.multiselect(
            "Activity Type",
            options=df[activity_col].unique(),
            default=df[activity_col].unique()
        )
        df_filtered = df_filtered[df_filtered[activity_col].isin(selected_activities)]
    
    if gear_col:
        gear_options = [x for x in df_filtered[gear_col].unique() if pd.notna(x)]
        if gear_options:
            selected_gear = st.sidebar.multiselect(
                "Gear",
                options=gear_options,
                default=gear_options
            )
            df_filtered = df_filtered[df_filtered[gear_col].isin(selected_gear)]
    
    if date_col:
        min_date = df_filtered[date_col].min()
        max_date = df_filtered[date_col].max()
        date_range = st.sidebar.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
        if len(date_range) == 2:
            df_filtered = df_filtered[
                (df_filtered[date_col].dt.date >= date_range[0]) &
                (df_filtered[date_col].dt.date <= date_range[1])
            ]
    
    if distance_col:
        min_dist = float(df_filtered[distance_col].min())
        max_dist = float(df_filtered[distance_col].max())
        dist_range = st.sidebar.slider(
            "Distance Range (km)",
            min_value=min_dist,
            max_value=max_dist,
            value=(min_dist, max_dist),
            step=0.1
        )
        df_filtered = df_filtered[
            (df_filtered[distance_col] >= dist_range[0]) &
            (df_filtered[distance_col] <= dist_range[1])
        ]
    
    # Summary metrics
    st.header("📊 Summary Statistics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Activities", len(df_filtered))
    
    with col2:
        if distance_col:
            st.metric("Total Distance", f"{df_filtered[distance_col].sum():.1f} km")
    
    with col3:
        if elevation_col:
            st.metric("Total Elevation", f"{df_filtered[elevation_col].sum():.0f} m")
    
    with col4:
        if calorie_col:
            st.metric("Total Calories", f"{df_filtered[calorie_col].sum():.0f} kcal")
    
    with col5:
        if hr_col:
            st.metric("Avg HR", f"{df_filtered[hr_col].mean():.0f} bpm")
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        ["Distance", "Activities", "Heart Rate", "Calories", "Elevation", "Weekly", "Data"]
    )
    
    with tab1:
        st.subheader("Distance Over Time")
        if date_col and distance_col:
            df_sorted = df_filtered.sort_values(date_col)
            fig = px.line(df_sorted, x=date_col, y=distance_col, markers=True,
                         title="Distance Timeline", labels={distance_col: "Distance (km)"})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Activity Breakdown")
        if activity_col:
            activity_counts = df_filtered[activity_col].value_counts()
            fig = px.pie(values=activity_counts.values, names=activity_counts.index,
                        title="Activities by Type")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Heart Rate Analysis")
        if hr_col:
            fig = px.histogram(df_filtered, x=hr_col, nbins=30,
                             title="HR Distribution", labels={hr_col: "Avg HR (bpm)"})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.subheader("Calorie Burn")
        if calorie_col:
            fig = px.histogram(df_filtered, x=calorie_col, nbins=30,
                             title="Calorie Distribution", labels={calorie_col: "Calories (kcal)"})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("Elevation Analysis")
        if elevation_col:
            fig = px.histogram(df_filtered, x=elevation_col, nbins=30,
                             title="Elevation Distribution", labels={elevation_col: "Elevation (m)"})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab6:
        st.subheader("Weekly Performance")
        if 'Day of Week' in df_filtered.columns:
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day_counts = df_filtered['Day of Week'].value_counts().reindex(day_order, fill_value=0)
            fig = px.bar(x=day_order, y=[day_counts[day] for day in day_order],
                        title="Activities by Day", labels={'x': 'Day', 'y': 'Count'})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab7:
        st.subheader("Activity Data")
        st.dataframe(df_filtered, use_container_width=True, height=400)
        csv = df_filtered.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "activities.csv", "text/csv")

else:
    st.info("👈 Upload a Strava CSV file to get started!")
