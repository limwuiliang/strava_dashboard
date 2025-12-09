import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import io

# Page configuration
st.set_page_config(
    page_title="Strava Activities Dashboard",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
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
    help="Export your activities from Strava and upload the CSV file here"
)

# Initialize session state for data
if uploaded_file is not None:
    # Load and process data
    @st.cache_data
    def load_data(file):
        df = pd.read_csv(file)
        return df
    
    df = load_data(uploaded_file)
    
    # Data preprocessing
    @st.cache_data
    def preprocess_data(df):
        df_processed = df.copy()
        
        # Convert date column to datetime
        if 'Activity Date' in df_processed.columns:
            df_processed['Activity Date'] = pd.to_datetime(df_processed['Activity Date'])
        elif 'Date' in df_processed.columns:
            df_processed['Date'] = pd.to_datetime(df_processed['Date'])
        
        # Handle distance column - convert to numeric
        distance_cols = [col for col in df_processed.columns if 'distance' in col.lower()]
        for col in distance_cols:
            if df_processed[col].dtype == 'object':
                df_processed[col] = pd.to_numeric(df_processed[col].str.replace(',', ''), errors='coerce')
        
        # Handle elevation column
        elevation_cols = [col for col in df_processed.columns if 'elevation' in col.lower()]
        for col in elevation_cols:
            if df_processed[col].dtype == 'object':
                df_processed[col] = pd.to_numeric(df_processed[col].str.replace(',', ''), errors='coerce')
        
        # Handle calories column
        calorie_cols = [col for col in df_processed.columns if 'calories' in col.lower() or 'kilocalories' in col.lower()]
        for col in calorie_cols:
            if df_processed[col].dtype == 'object':
                df_processed[col] = pd.to_numeric(df_processed[col].str.replace(',', ''), errors='coerce')
        
        # Handle HR columns
        hr_cols = [col for col in df_processed.columns if 'heart rate' in col.lower() or 'avg hr' in col.lower() or 'max hr' in col.lower()]
        for col in hr_cols:
            if df_processed[col].dtype == 'object':
                df_processed[col] = pd.to_numeric(df_processed[col].str.replace(',', ''), errors='coerce')
        
        # Handle time columns
        time_cols = [col for col in df_processed.columns if 'moving time' in col.lower() or 'elapsed time' in col.lower()]
        for col in time_cols:
            if df_processed[col].dtype == 'object':
                try:
                    df_processed[col] = pd.to_timedelta(df_processed[col])
                except:
                    pass
        
        return df_processed
    
    df = preprocess_data(df)
    
    # Get column names dynamically
    date_col = 'Activity Date' if 'Activity Date' in df.columns else 'Date' if 'Date' in df.columns else None
    
    distance_col = None
    for col in df.columns:
        if 'distance' in col.lower():
            distance_col = col
            break
    
    activity_col = 'Activity Type' if 'Activity Type' in df.columns else 'Type' if 'Type' in df.columns else None
    
    elevation_col = None
    for col in df.columns:
        if 'elevation' in col.lower():
            elevation_col = col
            break
    
    moving_time_col = None
    for col in df.columns:
        if 'moving time' in col.lower():
            moving_time_col = col
            break
    
    # Get calorie column
    calorie_col = None
    for col in df.columns:
        if 'calories' in col.lower() or 'kilocalories' in col.lower():
            calorie_col = col
            break
    
    # Get HR columns
    avg_hr_col = None
    max_hr_col = None
    for col in df.columns:
        if 'avg' in col.lower() and 'heart rate' in col.lower():
            avg_hr_col = col
        if 'max' in col.lower() and 'heart rate' in col.lower():
            max_hr_col = col
    
    # Get gear column
    gear_col = None
    for col in df.columns:
        if 'gear' in col.lower():
            gear_col = col
            break
    
    # Add day of week column
    if date_col and date_col in df.columns:
        df['Day of Week'] = df[date_col].dt.day_name()
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    if activity_col and activity_col in df.columns:
        selected_activities = st.sidebar.multiselect(
            "Activity Type",
            options=df[activity_col].unique(),
            default=df[activity_col].unique()
        )
        df_filtered = df[df[activity_col].isin(selected_activities)]
    else:
        df_filtered = df
    
    # Gear filter
    if gear_col and gear_col in df_filtered.columns:
        gear_options = [x for x in df_filtered[gear_col].unique() if pd.notna(x)]
        if gear_options:
            selected_gear = st.sidebar.multiselect(
                "Gear",
                options=gear_options,
                default=gear_options
            )
            df_filtered = df_filtered[df_filtered[gear_col].isin(selected_gear)]
    
    # Date range filter
    if date_col and date_col in df_filtered.columns:
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
    
    # Distance range filter
    if distance_col and distance_col in df_filtered.columns:
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
    
    # Display data summary
    st.header("📊 Summary Statistics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Total Activities",
            value=len(df_filtered),
            delta=f"{len(df_filtered)} activities"
        )
    
    with col2:
        if distance_col and distance_col in df_filtered.columns:
            total_distance = df_filtered[distance_col].sum()
            st.metric(
                label="Total Distance",
                value=f"{total_distance:.1f} km",
                delta=f"{total_distance:.1f} km"
            )
    
    with col3:
        if elevation_col and elevation_col in df_filtered.columns:
            total_elevation = df_filtered[elevation_col].sum()
            st.metric(
                label="Total Elevation",
                value=f"{total_elevation:.0f} m",
                delta=f"{total_elevation:.0f} m"
            )
    
    with col4:
        if calorie_col and calorie_col in df_filtered.columns:
            total_calories = df_filtered[calorie_col].sum()
            st.metric(
                label="Total Calories",
                value=f"{total_calories:.0f} kcal",
                delta=f"{total_calories:.0f} kcal"
            )
    
    with col5:
        if avg_hr_col and avg_hr_col in df_filtered.columns:
            avg_hr = df_filtered[avg_hr_col].mean()
            st.metric(
                label="Avg Heart Rate",
                value=f"{avg_hr:.0f} bpm",
                delta=f"{avg_hr:.0f} bpm"
            )
    
    # Charts section
    st.header("📈 Visualizations")
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        ["Distance Trends", "Activity Breakdown", "Heart Rate Analysis", "Calorie Burn", "Elevation Analysis", "Weekly Performance", "Data Table"]
    )
    
    with tab1:
        st.subheader("Distance Over Time")
        if date_col and distance_col and date_col in df_filtered.columns and distance_col in df_filtered.columns:
            df_sorted = df_filtered.sort_values(date_col)
            
            fig = px.line(
                df_sorted,
                x=date_col,
                y=distance_col,
                title="Activity Distance Timeline",
                labels={distance_col: "Distance (km)", date_col: "Date"},
                markers=True,
                color_discrete_sequence=["#FC5200"]
            )
            fig.update_layout(hovermode='x unified', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cumulative distance
            df_sorted['Cumulative Distance'] = df_sorted[distance_col].cumsum()
            fig_cumulative = px.line(
                df_sorted,
                x=date_col,
                y='Cumulative Distance',
                title="Cumulative Distance Over Time",
                labels={'Cumulative Distance': "Cumulative Distance (km)", date_col: "Date"},
                color_discrete_sequence=["#00A8E8"]
            )
            fig_cumulative.update_layout(hovermode='x unified', height=500)
            st.plotly_chart(fig_cumulative, use_container_width=True)
    
    with tab2:
        st.subheader("Activity Type Distribution")
        if activity_col and activity_col in df_filtered.columns:
            activity_counts = df_filtered[activity_col].value_counts()
            
            fig = px.pie(
                values=activity_counts.values,
                names=activity_counts.index,
                title="Activities by Type",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Distance by activity type
            if distance_col and distance_col in df_filtered.columns:
                activity_distance = df_filtered.groupby(activity_col)[distance_col].sum().sort_values(ascending=False)
                
                fig_bar = px.bar(
                    x=activity_distance.values,
                    y=activity_distance.index,
                    orientation='h',
                    title="Total Distance by Activity Type",
                    labels={'x': "Distance (km)", 'y': "Activity Type"},
                    color=activity_distance.values,
                    color_continuous_scale="Viridis"
                )
                st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab3:
        st.subheader("Heart Rate Analysis")
        if avg_hr_col and avg_hr_col in df_filtered.columns:
            # HR distribution histogram
            fig_hr_dist = px.histogram(
                df_filtered,
                x=avg_hr_col,
                nbins=30,
                title="Average Heart Rate Distribution",
                labels={avg_hr_col: "Average Heart Rate (bpm)", 'count': "Number of Activities"},
                color_discrete_sequence=["#E63946"]
            )
            st.plotly_chart(fig_hr_dist, use_container_width=True)
            
            # HR over time
            if date_col and date_col in df_filtered.columns:
                df_sorted_hr = df_filtered.sort_values(date_col)
                fig_hr_time = px.line(
                    df_sorted_hr,
                    x=date_col,
                    y=avg_hr_col,
                    title="Average Heart Rate Over Time",
                    labels={avg_hr_col: "Avg HR (bpm)", date_col: "Date"},
                    markers=True,
                    color_discrete_sequence=["#E63946"]
                )
                fig_hr_time.update_layout(hovermode='x unified', height=500)
                st.plotly_chart(fig_hr_time, use_container_width=True)
        
        # Max HR analysis
        if max_hr_col and max_hr_col in df_filtered.columns:
            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    label="Max Heart Rate",
                    value=f"{df_filtered[max_hr_col].max():.0f} bpm"
                )
            with col2:
                st.metric(
                    label="Avg Max Heart Rate",
                    value=f"{df_filtered[max_hr_col].mean():.0f} bpm"
                )
    
    with tab4:
        st.subheader("Calorie Burn Analysis")
        if calorie_col and calorie_col in df_filtered.columns:
            # Calorie distribution
            fig_cal_dist = px.histogram(
                df_filtered,
                x=calorie_col,
                nbins=30,
                title="Calorie Burn Distribution",
                labels={calorie_col: "Calories (kcal)", 'count': "Number of Activities"},
                color_discrete_sequence=["#F77F00"]
            )
            st.plotly_chart(fig_cal_dist, use_container_width=True)
            
            # Calories over time
            if date_col and date_col in df_filtered.columns:
                df_sorted_cal = df_filtered.sort_values(date_col)
                fig_cal_time = px.line(
                    df_sorted_cal,
                    x=date_col,
                    y=calorie_col,
                    title="Calorie Burn Over Time",
                    labels={calorie_col: "Calories (kcal)", date_col: "Date"},
                    markers=True,
                    color_discrete_sequence=["#F77F00"]
                )
                fig_cal_time.update_layout(hovermode='x unified', height=500)
                st.plotly_chart(fig_cal_time, use_container_width=True)
            
            # Calories by activity type
            if activity_col and activity_col in df_filtered.columns:
                cal_by_activity = df_filtered.groupby(activity_col)[calorie_col].sum().sort_values(ascending=False)
                fig_cal_activity = px.bar(
                    x=cal_by_activity.values,
                    y=cal_by_activity.index,
                    orientation='h',
                    title="Total Calories Burned by Activity Type",
                    labels={'x': "Calories (kcal)", 'y': "Activity Type"},
                    color=cal_by_activity.values,
                    color_continuous_scale="Oranges"
                )
                st.plotly_chart(fig_cal_activity, use_container_width=True)
    
    with tab5:
        st.subheader("Elevation Analysis")
        if elevation_col and elevation_col in df_filtered.columns:
            fig = px.histogram(
                df_filtered,
                x=elevation_col,
                nbins=30,
                title="Elevation Gain Distribution",
                labels={elevation_col: "Elevation Gain (m)", 'count': "Number of Activities"},
                color_discrete_sequence=["#06A77D"]
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Elevation vs Distance scatter
            if distance_col and distance_col in df_filtered.columns:
                fig_scatter = px.scatter(
                    df_filtered,
                    x=distance_col,
                    y=elevation_col,
                    title="Elevation Gain vs Distance",
                    labels={distance_col: "Distance (km)", elevation_col: "Elevation Gain (m)"},
                    color_discrete_sequence=["#D62828"],
                    size=distance_col,
                    hover_data=[activity_col] if activity_col else None
                )
                st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab6:
        st.subheader("Best Performing Days of the Week")
        if 'Day of Week' in df_filtered.columns:
            # Define day order
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            
            # Activities by day of week
            day_activity_count = df_filtered['Day of Week'].value_counts().reindex(day_order, fill_value=0)
            
            fig_day_count = px.bar(
                x=day_order,
                y=[day_activity_count[day] for day in day_order],
                title="Number of Activities by Day of Week",
                labels={'x': "Day of Week", 'y': "Number of Activities"},
                color=[day_activity_count[day] for day in day_order],
                color_continuous_scale="Blues"
            )
            st.plotly_chart(fig_day_count, use_container_width=True)
            
            # Distance by day of week
            if distance_col and distance_col in df_filtered.columns:
                day_distance = df_filtered.groupby('Day of Week')[distance_col].sum().reindex(day_order, fill_value=0)
                
                fig_day_dist = px.bar(
                    x=day_order,
                    y=[day_distance[day] for day in day_order],
                    title="Total Distance by Day of Week",
                    labels={'x': "Day of Week", 'y': "Distance (km)"},
                    color=[day_distance[day] for day in day_order],
                    color_continuous_scale="Greens"
                )
                st.plotly_chart(fig_day_dist, use_container_width=True)
            
            # Calories by day of week
            if calorie_col and calorie_col in df_filtered.columns:
                day_calories = df_filtered.groupby('Day of Week')[calorie_col].sum().reindex(day_order, fill_value=0)
                
                fig_day_cal = px.bar(
                    x=day_order,
                    y=[day_calories[day] for day in day_order],
                    title="Total Calories Burned by Day of Week",
                    labels={'x': "Day of Week", 'y': "Calories (kcal)"},
                    color=[day_calories[day] for day in day_order],
                    color_continuous_scale="Oranges"
                )
                st.plotly_chart(fig_day_cal, use_container_width=True)
            
            # Average HR by day of week
            if avg_hr_col and avg_hr_col in df_filtered.columns:
                day_avg_hr = df_filtered.groupby('Day of Week')[avg_hr_col].mean().reindex(day_order, fill_value=0)
                
                fig_day_hr = px.bar(
                    x=day_order,
                    y=[day_avg_hr[day] for day in day_order],
                    title="Average Heart Rate by Day of Week",
                    labels={'x': "Day of Week", 'y': "Avg HR (bpm)"},
                    color=[day_avg_hr[day] for day in day_order],
                    color_continuous_scale="Reds"
                )
                st.plotly_chart(fig_day_hr, use_container_width=True)
    
    with tab7:
        st.subheader("Detailed Activity Data")
        
        # Display filtered data
        display_cols = [col for col in df_filtered.columns if col not in ['Day of Week']]
        st.dataframe(df_filtered[display_cols], use_container_width=True, height=400)
        
        # Download button
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name=f"strava_filtered_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    # Additional insights
    st.header("💡 Key Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if distance_col and distance_col in df_filtered.columns:
            longest_activity = df_filtered.loc[df_filtered[distance_col].idxmax()]
            st.info(f"""
            **Longest Activity**: {longest_activity[distance_col]:.1f} km
            {f"({longest_activity[activity_col]})" if activity_col and activity_col in df_filtered.columns else ""}
            """)
    
    with col2:
        if elevation_col and elevation_col in df_filtered.columns:
            highest_elevation = df_filtered.loc[df_filtered[elevation_col].idxmax()]
            st.info(f"""
            **Highest Elevation Gain**: {highest_elevation[elevation_col]:.0f} m
            {f"({highest_elevation[activity_col]})" if activity_col and activity_col in df_filtered.columns else ""}
            """)
    
    with col3:
        if calorie_col and calorie_col in df_filtered.columns:
            highest_calories = df_filtered.loc[df_filtered[calorie_col].idxmax()]
            st.info(f"""
            **Most Calories Burned**: {highest_calories[calorie_col]:.0f} kcal
            {f"({highest_calories[activity_col]})" if activity_col and activity_col in df_filtered.columns else ""}
            """)
    
    # Show data info
    with st.expander("📋 Data Information"):
        st.write(f"**Total rows loaded**: {len(df)}")
        st.write(f"**Rows after filtering**: {len(df_filtered)}")
        st.write(f"**Columns in dataset**: {len(df.columns)}")
        st.write("**Column names:**")
        st.write(df.columns.tolist())

else:
    # Show welcome message when no file is uploaded
    st.info("👈 Please upload a Strava activities CSV file using the sidebar to get started!")
    
    st.markdown("""
    ## How to use this dashboard:
    
    1. **Export your data from Strava**:
       - Go to your Strava profile settings
       - Navigate to "My Account" → "Download or Delete Your Account"
       - Click "Request your archive"
       - You'll receive an email with a download link (may take a few hours)
       - Extract the ZIP file and look for the activities CSV file
    
    2. **Upload the CSV file** using the file uploader in the sidebar
    
    3. **Explore your data**:
       - Use the filters to narrow down by activity type, date range, distance, or gear
       - View interactive charts showing your fitness trends
       - Check heart rate, calorie burn, and elevation analysis
       - See your best performing days of the week
       - Download filtered data for further analysis
    
    ## Features:
    - 📊 Interactive distance trends and cumulative progress
    - 🎯 Activity type breakdown and distribution
    - ❤️ Heart rate analysis with average and max HR tracking
    - 🔥 Calorie burn analysis and trends
    - ⛰️ Elevation gain analysis
    - 📅 Weekly performance insights - best performing days
    - 🎽 Filterable by gear type
    - 📥 Download filtered data
    - 🔍 Customizable filters for date range, activity type, distance, and gear
    """)
