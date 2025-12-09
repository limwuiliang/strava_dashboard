# 🏃 Strava Activities Dashboard

A comprehensive Streamlit application for analyzing and visualizing your Strava fitness activities data. Upload your CSV export and gain insights into your training patterns, performance metrics, and fitness trends.

## ✨ Features

### 📊 Analytics & Visualizations
- **Distance Trends**: Track distance over time with cumulative progress visualization
- **Activity Type Breakdown**: See the distribution of your different activity types
- **Heart Rate Analysis**: Monitor average and maximum heart rate patterns
- **Calorie Burn Analysis**: Track calories burned across activities and time
- **Elevation Analysis**: Analyze elevation gains and correlations with distance
- **Weekly Performance**: Identify your best performing days of the week
- **Detailed Data Table**: View and export all your activity data

### 🔍 Interactive Filters
- **Activity Type**: Filter by running, cycling, swimming, etc.
- **Date Range**: Select specific time periods for analysis
- **Distance Range**: Focus on activities within a certain distance
- **Gear**: Filter activities by the gear/equipment used

### 📥 Data Export
- Download filtered data as CSV for further analysis
- Maintain data integrity with proper numeric conversions

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/strava-dashboard.git
   cd strava-dashboard
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`

### Deploy to Streamlit Cloud

1. **Push to GitHub**
   - Ensure your repository is public or add Streamlit Cloud as a collaborator
   - Push all files including `requirements.txt`

2. **Connect to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://share.streamlit.io/)
   - Click "New app"
   - Select your GitHub repository, branch, and `streamlit_app.py` as the main file
   - Click "Deploy"

3. **Share your app**
   - Your app will be live at `https://share.streamlit.io/yourusername/strava-dashboard`

## 📋 How to Export Your Strava Data

1. **Log in to Strava** at strava.com
2. **Go to Settings** (click your profile icon → Settings)
3. **Navigate to "My Account"** tab
4. **Click "Download or Delete Your Account"**
5. **Select "Request your archive"**
6. **Check your email** for a download link (may take a few hours)
7. **Extract the ZIP file** and locate the `activities.csv` file
8. **Upload the CSV** to this dashboard

## 📊 Supported Data Fields

The dashboard automatically detects and processes these fields from your Strava export:

- **Activity Date**: Date of the activity
- **Activity Type**: Type of activity (Run, Ride, Swim, etc.)
- **Distance**: Distance covered (in km)
- **Elevation Gain**: Total elevation gain (in meters)
- **Moving Time**: Time spent moving
- **Elapsed Time**: Total elapsed time
- **Average Heart Rate**: Average HR during activity
- **Max Heart Rate**: Maximum HR during activity
- **Calories**: Calories burned
- **Gear**: Equipment used for the activity

*Note: Not all fields are required. The dashboard will work with whatever data you have available.*

## 🎨 Customization

### Change Theme Colors
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FC5200"      # Change primary color
backgroundColor = "#FFFFFF"   # Change background
textColor = "#262730"         # Change text color
```

### Modify Chart Colors
Edit the color schemes in `app.py` by changing the `color_discrete_sequence` parameters in the plotly charts.

## 📦 Requirements

- Python 3.7+
- streamlit >= 1.28.1
- pandas >= 2.1.3
- plotly >= 5.18.0
- numpy >= 1.24.3

## 🐛 Troubleshooting

### "Column not found" errors
- Ensure your CSV export includes the expected columns
- Check that column names match Strava's standard export format
- The app will work with any subset of columns

### Data not displaying correctly
- Verify your CSV file is not corrupted
- Check that numeric fields don't have unexpected formatting
- Try re-exporting your data from Strava

### Performance issues with large datasets
- The app uses caching to improve performance
- Clear cache if needed: `streamlit cache clear`
- Consider filtering to a specific date range

## 📝 Project Structure

```
strava-dashboard/
├── app.py                    # Main Streamlit application
├── streamlit_app.py         # Entry point for Streamlit Cloud
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Strava](https://www.strava.com/) for the fitness data platform
- [Streamlit](https://streamlit.io/) for the amazing framework
- [Plotly](https://plotly.com/) for interactive visualizations

## 📧 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review your CSV export format
3. Open an issue on GitHub

---

**Happy tracking! 🏃‍♂️🚴‍♀️🏊‍♂️**
