# Quick Start Guide

## Run Locally (5 minutes)

### 1. Install Dependencies

```bash
cd streamlit_app
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

### 3. Open in Browser

App automatically opens at: `http://localhost:8501`

### 4. Generate a Report

1. Click **"Press Premium SVOD Update"** in sidebar
2. Click **"🚀 Generate Report"** button
3. Wait 30-60 seconds for data processing
4. View interactive dashboard
5. Download Excel file

---

## Deploy to Cloud (10 minutes)

### 1. Push to GitHub

```bash
git add streamlit_app/
git commit -m "Add Streamlit web app"
git push origin main
```

### 2. Deploy to Streamlit Cloud

1. Visit: https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - Repository: `AntennaAnalytics/Slide-Production`
   - Branch: `main`
   - Main file: `streamlit_app/app.py`
5. Click "Deploy"

### 3. Share the URL

Your app is live at: `https://[your-app-name].streamlit.app`

---

## What You Get

✅ **Self-Service Reports**: Generate reports with one click
✅ **Interactive Dashboard**: View data in browser
✅ **Downloadable Excel**: Get formatted Excel files
✅ **100% Python**: No JavaScript needed
✅ **Cloud Hosting**: Free on Streamlit Community Cloud

---

## Next Steps

- Read [README.md](README.md) for full documentation
- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment guide
- Test locally with `test_report.py`

---

## Troubleshooting

**App won't start?**
- Run: `pip install -r requirements.txt`
- Check Python version: `python --version` (need 3.8+)

**Report generation fails?**
- Verify Redash API is accessible
- Check internet connection
- Ensure template file exists in `../templates/`

**Need help?**
- Check logs in terminal (local) or Streamlit Cloud dashboard (cloud)
- Review [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting section
