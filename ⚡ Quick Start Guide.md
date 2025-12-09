# ⚡ Quick Start Guide

Get your Strava Activities Dashboard up and running in minutes!

## 🚀 Fastest Way: Deploy to Streamlit Cloud (Recommended)

### 1. Create a GitHub Repository
- Go to https://github.com/new
- Name it `strava-dashboard`
- Make it **Public**
- Click "Create repository"

### 2. Upload Files
- Click "Add file" → "Upload files"
- Upload all files from this project:
  - `app.py`
  - `streamlit_app.py`
  - `requirements.txt`
  - `.streamlit/config.toml`
  - `.gitignore`
  - `README.md`

### 3. Deploy to Streamlit Cloud
- Go to https://share.streamlit.io
- Click "New app"
- Select your repository
- Set main file to `streamlit_app.py`
- Click "Deploy"
- Wait 2-3 minutes for deployment

### 4. Get Your Data
- Go to https://www.strava.com
- Settings → My Account
- Click "Download or Delete Your Account"
- Click "Request your archive"
- Check your email for download link (may take hours)
- Extract and find `activities.csv`

### 5. Use Your Dashboard
- Open your Streamlit Cloud URL
- Upload your `activities.csv`
- Explore your fitness data!

---

## 💻 Local Development: Run Locally

### 1. Install Python
- Download Python 3.7+ from https://python.org

### 2. Clone/Download This Project
```bash
git clone https://github.com/YOUR_USERNAME/strava-dashboard.git
cd strava-dashboard
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

### 5. Open in Browser
- App opens automatically at `http://localhost:8501`
- Upload your Strava CSV file
- Enjoy your dashboard!

---

## 📊 What You'll See

After uploading your Strava data, you get:

✅ **Summary Statistics**
- Total activities, distance, elevation, calories, heart rate

✅ **Distance Trends**
- Line charts showing distance over time
- Cumulative progress tracker

✅ **Activity Breakdown**
- Pie chart of activity types
- Distance by activity type

✅ **Heart Rate Analysis**
- HR distribution histogram
- HR trends over time
- Max HR tracking

✅ **Calorie Burn**
- Calorie distribution
- Calories over time
- Calories by activity type

✅ **Elevation Analysis**
- Elevation gain distribution
- Elevation vs distance scatter plot

✅ **Weekly Performance**
- Best performing days of the week
- Activities, distance, calories, and HR by day

✅ **Filters**
- Activity type
- Date range
- Distance range
- Gear type

✅ **Data Export**
- Download filtered data as CSV

---

## 🆘 Troubleshooting

### "Column not found" error
→ Your CSV might have different column names. The app will work with any columns you have.

### App won't load
→ Check that `requirements.txt` is in your GitHub repo
→ Make sure repository is **Public**

### Can't find Strava export
→ Go to strava.com → Settings → My Account
→ Click "Download or Delete Your Account"
→ Click "Request your archive"
→ Check email (may take several hours)

### Data not showing
→ Make sure CSV file has data
→ Try sample data: run `python sample_data_generator.py`

---

## 📚 Next Steps

1. **Customize colors**: Edit `.streamlit/config.toml`
2. **Add features**: Edit `app.py` to add new visualizations
3. **Share with friends**: Send them your Streamlit Cloud URL
4. **Deploy updates**: Push changes to GitHub, Streamlit auto-deploys

---

## 📖 Full Documentation

See `README.md` for complete documentation and advanced features.

---

**Happy tracking! 🏃‍♂️🚴‍♀️🏊‍♂️**
