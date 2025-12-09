# 🎯 Strava Activities Dashboard - Complete Setup Instructions

Congratulations! You now have a complete, production-ready Streamlit application for analyzing your Strava fitness data. Here's everything you need to know to get started.

---

## 📦 What You're Getting

A fully functional Streamlit dashboard with:

✅ **7 Interactive Visualization Tabs**
- Distance Trends (with cumulative tracking)
- Activity Type Breakdown
- Heart Rate Analysis
- Calorie Burn Analysis
- Elevation Analysis
- Best Performing Days of the Week
- Detailed Data Table with export

✅ **Advanced Filtering**
- Activity Type filter
- Date Range picker
- Distance Range slider
- Gear Type filter

✅ **Key Metrics & Insights**
- Summary statistics dashboard
- Key insights cards
- Detailed data information

✅ **Data Export**
- Download filtered data as CSV
- Maintain data integrity

---

## 🚀 Quick Start (Choose One)

### Option 1: Deploy to Streamlit Cloud (Easiest - 5 minutes)

**Best for:** Sharing with others, no local setup needed

1. **Create GitHub Repository**
   ```
   Go to https://github.com/new
   - Name: strava-dashboard
   - Make it PUBLIC
   - Create repository
   ```

2. **Upload Files**
   - Click "Add file" → "Upload files"
   - Upload all files from the `strava_dashboard` folder:
     - `app.py`
     - `streamlit_app.py`
     - `requirements.txt`
     - `.streamlit/config.toml`
     - `.gitignore`
     - `README.md`
     - `DEPLOYMENT.md`
     - `QUICKSTART.md`
     - `sample_data_generator.py`
     - `.github/workflows/python-app.yml`

3. **Deploy**
   ```
   Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file to: streamlit_app.py
   - Click "Deploy"
   - Wait 2-3 minutes
   ```

4. **Get Your Live URL**
   - Streamlit will give you a URL like:
   - `https://share.streamlit.io/YOUR_USERNAME/strava-dashboard`
   - Share this with anyone!

---

### Option 2: Run Locally (10 minutes)

**Best for:** Development, testing, privacy

1. **Install Python**
   - Download from https://python.org (3.7 or higher)
   - Install with default settings

2. **Download Project**
   - Extract the `strava_dashboard` folder
   - Open terminal/command prompt in that folder

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

5. **Access Dashboard**
   - Opens automatically at `http://localhost:8501`
   - Upload your Strava CSV file
   - Start analyzing!

---

## 📊 Getting Your Strava Data

### Step 1: Request Your Data Export
1. Go to https://www.strava.com
2. Click your profile icon (top right)
3. Click "Settings"
4. Click "My Account" (in left sidebar)
5. Scroll down to "Download or Delete Your Account"
6. Click "Get Started"
7. Click "Request your archive"

### Step 2: Wait for Email
- Strava will email you a download link
- **This may take several hours** (sometimes up to 24 hours)
- Check your email (including spam folder)

### Step 3: Extract and Find CSV
1. Download the ZIP file from the email link
2. Extract the ZIP file
3. Look for `activities.csv` file
4. This is the file you'll upload to the dashboard

---

## 📈 Using the Dashboard

### Upload Your Data
1. Open the dashboard (local or Streamlit Cloud)
2. Click the file uploader in the left sidebar
3. Select your `activities.csv` file
4. The dashboard loads automatically

### Explore Your Data
1. **Summary Statistics** - See your key metrics at a glance
2. **Distance Trends** - Track your distance over time
3. **Activity Breakdown** - See which activities you do most
4. **Heart Rate Analysis** - Monitor your HR patterns
5. **Calorie Burn** - Track calories burned
6. **Elevation Analysis** - See your hilliest workouts
7. **Weekly Performance** - Find your best days
8. **Data Table** - View all activities and export

### Use Filters
- **Activity Type**: Focus on specific activities
- **Date Range**: Analyze specific time periods
- **Distance Range**: Look at activities of certain lengths
- **Gear**: See stats for specific equipment

### Export Data
- Click "Download Filtered Data as CSV"
- Use in Excel, Google Sheets, or other tools

---

## 🛠️ Project Structure

```
strava_dashboard/
├── app.py                          # Main application (23KB)
├── streamlit_app.py               # Streamlit Cloud entry point
├── requirements.txt               # Python dependencies
├── README.md                      # Full documentation
├── QUICKSTART.md                  # Quick start guide
├── DEPLOYMENT.md                  # Deployment guide
├── sample_data_generator.py       # Generate test data
├── sample_strava_data.csv         # Sample data for testing
├── .streamlit/
│   └── config.toml               # Streamlit theme config
├── .github/
│   └── workflows/
│       └── python-app.yml        # GitHub Actions CI/CD
└── .gitignore                    # Git ignore rules
```

---

## 🔧 Customization

### Change Colors
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FC5200"      # Orange (Strava color)
backgroundColor = "#FFFFFF"   # White
secondaryBackgroundColor = "#F0F2F6"  # Light gray
textColor = "#262730"         # Dark gray
```

### Add New Charts
Edit `app.py` and add new Plotly charts in the appropriate tabs.

### Modify Filters
Edit the sidebar filter section in `app.py` to add/remove filters.

---

## 🚨 Troubleshooting

### "Column not found" Error
**Problem:** CSV has different column names
**Solution:** The app auto-detects columns. Check your CSV headers match Strava's format.

### App Won't Load
**Problem:** Dependencies not installed
**Solution:** Run `pip install -r requirements.txt`

### Can't Find Strava Export
**Problem:** Email not received
**Solution:** 
- Check spam folder
- Wait longer (can take 24 hours)
- Try requesting again from Strava settings

### Data Not Showing
**Problem:** CSV file is empty or corrupted
**Solution:** 
- Try uploading `sample_strava_data.csv` to test
- Re-export from Strava

### Performance Issues
**Problem:** App is slow with large CSV
**Solution:**
- Filter to specific date range
- Streamlit caches data automatically
- Try running locally instead of cloud

---

## 📱 Sharing Your Dashboard

### Streamlit Cloud
- Share the URL: `https://share.streamlit.io/YOUR_USERNAME/strava-dashboard`
- Anyone can access and upload their own data
- Data is NOT stored on servers (only in browser)

### Local Network
- Run `streamlit run app.py --server.address 0.0.0.0`
- Share your computer's IP address
- Others can access from same network

### GitHub
- Push to GitHub
- Others can fork or clone
- Deploy their own version

---

## 🔒 Privacy & Security

✅ **Your data is safe:**
- Data is only stored in your browser session
- NOT sent to any external servers
- Cleared when you refresh the page
- Streamlit Cloud doesn't store uploads

✅ **How it works:**
- You upload CSV to your browser
- Browser processes the data locally
- Charts render in your browser
- No server-side data storage

---

## 📚 File Descriptions

| File | Purpose | Size |
|------|---------|------|
| `app.py` | Main application code | 23 KB |
| `streamlit_app.py` | Streamlit Cloud entry point | 106 B |
| `requirements.txt` | Python package dependencies | 61 B |
| `README.md` | Complete documentation | 5.6 KB |
| `QUICKSTART.md` | Quick start guide | 3.5 KB |
| `DEPLOYMENT.md` | Deployment instructions | 4 KB |
| `sample_data_generator.py` | Test data generator | 2.3 KB |
| `sample_strava_data.csv` | Sample data for testing | 8.6 KB |
| `.streamlit/config.toml` | Streamlit configuration | 199 B |
| `.github/workflows/python-app.yml` | CI/CD workflow | 924 B |
| `.gitignore` | Git ignore rules | 1.4 KB |

---

## 🆘 Getting Help

### Documentation
- `README.md` - Full feature documentation
- `QUICKSTART.md` - Quick start guide
- `DEPLOYMENT.md` - Deployment guide

### Resources
- Streamlit Docs: https://docs.streamlit.io
- Plotly Docs: https://plotly.com/python/
- Strava Support: https://support.strava.com

### Common Issues
- Check the Troubleshooting section above
- Review your CSV format
- Try with sample data first

---

## 🎉 Next Steps

1. **Deploy to Streamlit Cloud** (recommended)
   - Follow Option 1 above
   - Share your URL with friends

2. **Get Your Strava Data**
   - Follow the data export steps
   - Request your archive

3. **Upload and Explore**
   - Upload your CSV
   - Explore your fitness insights

4. **Customize**
   - Change colors in `config.toml`
   - Add new features to `app.py`
   - Deploy updates via GitHub

---

## 📞 Support

If you encounter issues:

1. **Check Troubleshooting** section above
2. **Review README.md** for detailed docs
3. **Try sample data** to test functionality
4. **Check Streamlit logs** for error messages

---

## 🎓 Learning Resources

Want to extend the dashboard?

- **Streamlit**: https://docs.streamlit.io
- **Plotly**: https://plotly.com/python/
- **Pandas**: https://pandas.pydata.org/docs/
- **Python**: https://python.org/docs/

---

## 🏁 You're All Set!

You now have everything you need to:
- ✅ Deploy a professional fitness dashboard
- ✅ Analyze your Strava activities
- ✅ Share insights with others
- ✅ Customize and extend the app

**Happy tracking! 🏃‍♂️🚴‍♀️🏊‍♂️**

---

**Questions?** Check the README.md or QUICKSTART.md files included in your project.
