# 🚀 Deployment Guide

This guide will help you deploy the Strava Activities Dashboard to Streamlit Cloud.

## Prerequisites

- GitHub account
- Streamlit Cloud account (free at https://share.streamlit.io)
- Your Strava data CSV file

## Step 1: Prepare Your GitHub Repository

### Option A: Create a New Repository

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Name it `strava-dashboard` (or your preferred name)
   - Make it **Public** (required for free Streamlit Cloud)
   - Initialize with README (optional)

2. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/strava-dashboard.git
   cd strava-dashboard
   ```

3. **Copy all files from this project**
   - Copy all files from the strava_dashboard folder into your cloned repository
   - Ensure you have:
     - `app.py`
     - `streamlit_app.py`
     - `requirements.txt`
     - `.streamlit/config.toml`
     - `.gitignore`
     - `README.md`
     - `.github/workflows/python-app.yml`

4. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: Strava Activities Dashboard"
   git push origin main
   ```

### Option B: Fork or Use as Template

If you want to use this as a template:
1. Click "Use this template" on the GitHub repository
2. Name your repository
3. Clone your new repository locally

## Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Sign in with your GitHub account (or create one)

2. **Create a new app**
   - Click "New app" button
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set the main file path to `streamlit_app.py`
   - Click "Deploy"

3. **Wait for deployment**
   - Streamlit will install dependencies and start your app
   - This usually takes 2-3 minutes
   - You'll see a live URL when complete

4. **Share your app**
   - Your app URL will be: `https://share.streamlit.io/YOUR_USERNAME/strava-dashboard`
   - Share this link with anyone to use your dashboard!

## Step 3: Using Your Deployed App

1. **Access the app**
   - Open the URL provided by Streamlit Cloud
   - The app is now live and accessible to anyone with the link

2. **Upload your Strava data**
   - Click the file uploader in the sidebar
   - Select your `activities.csv` file from your Strava export
   - The dashboard will load and display your data

3. **Explore your analytics**
   - Use the filters to customize your view
   - Interact with the charts
   - Download filtered data as needed

## Updating Your App

When you make changes to the code:

1. **Make changes locally**
   ```bash
   # Edit files as needed
   ```

2. **Commit and push to GitHub**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

3. **Streamlit Cloud will auto-deploy**
   - Your app will automatically update within a few minutes
   - No manual deployment needed!

## Troubleshooting

### App won't load
- Check the logs in Streamlit Cloud dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify `streamlit_app.py` exists and is correct

### Missing columns error
- Ensure your CSV has the expected column names
- Check Strava export format matches expectations
- See README.md for supported fields

### Performance issues
- Large CSV files may take time to load
- Try filtering to a specific date range
- Streamlit caches data automatically

### Data privacy
- Your data is only stored in your browser session
- No data is sent to external servers
- Each upload is temporary and cleared on page refresh

## Advanced: Custom Domain

If you want a custom domain (Streamlit Cloud Pro feature):

1. Subscribe to Streamlit Cloud Pro
2. Go to your app settings
3. Add your custom domain
4. Update DNS records as instructed

## Support

For issues with:
- **Streamlit**: https://docs.streamlit.io
- **Deployment**: https://docs.streamlit.io/streamlit-cloud
- **This app**: Check the README.md or open a GitHub issue

---

**Your Strava dashboard is now live! 🎉**
