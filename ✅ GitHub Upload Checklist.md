# ✅ GitHub Upload Checklist

Follow these steps to upload your Strava Dashboard to GitHub and deploy it.

---

## 📋 Step 1: Create GitHub Repository

- [ ] Go to https://github.com/new
- [ ] Name: `strava-dashboard`
- [ ] Description: "Strava Activities Dashboard - Analyze your fitness data"
- [ ] Make it **PUBLIC** ⭐ (required for free Streamlit Cloud)
- [ ] Click "Create repository"

---

## 📤 Step 2: Upload Files to GitHub

On your new repo page:

1. Click **"Add file"** → **"Upload files"**

### Root Level Files (upload directly)
- [ ] `app.py`
- [ ] `streamlit_app.py`
- [ ] `requirements.txt`
- [ ] `README.md`
- [ ] `QUICKSTART.md`
- [ ] `DEPLOYMENT.md`
- [ ] `sample_data_generator.py`
- [ ] `.gitignore`

### Folder: `.streamlit/`
- [ ] Create folder `.streamlit`
- [ ] Upload `config.toml` inside it

### Folder: `.github/workflows/`
- [ ] Create folder `.github`
- [ ] Inside `.github`, create folder `workflows`
- [ ] Upload `python-app.yml` inside `workflows`

### Optional (for testing)
- [ ] `sample_strava_data.csv` (sample data for testing)

---

## 🎯 Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click **"New app"** button
3. **Repository:** Select `strava-dashboard`
4. **Branch:** `main` (default)
5. **Main file path:** `streamlit_app.py` ⭐ (important!)
6. Click **"Deploy"**
7. Wait 2-3 minutes for deployment
8. Your live URL appears! 🎉

---

## 🔗 Your Live Dashboard

Once deployed, your URL will be:
```
https://share.streamlit.io/YOUR_GITHUB_USERNAME/strava-dashboard
```

**Share this URL with anyone to let them use your dashboard!**

---

## ✨ That's It!

Your Strava Activities Dashboard is now live and ready to use! 🚀

Next steps:
1. Get your Strava data (see QUICKSTART.md)
2. Upload your CSV to the dashboard
3. Explore your fitness insights!

---

## 🆘 Troubleshooting

**"Repository not found" error?**
- Make sure repo is **PUBLIC**
- Wait a few seconds and try again

**"Main file not found" error?**
- Check that `streamlit_app.py` is in the root directory
- Not in a subfolder

**App won't load?**
- Check Streamlit Cloud logs
- Verify `requirements.txt` is uploaded
- Make sure all files are in correct locations

---

**Questions?** See README.md or QUICKSTART.md in your repository.
