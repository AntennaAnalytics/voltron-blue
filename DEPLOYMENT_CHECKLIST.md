# Deployment Checklist

Use this checklist to deploy your Streamlit app to production.

## Pre-Deployment

### ✅ Code Complete
- [x] Streamlit app created (`app.py`)
- [x] Report module implemented (`reports/press_update_report.py`)
- [x] Requirements file created (`requirements.txt`)
- [x] Configuration files created (`.streamlit/config.toml`)
- [x] Documentation written (README, DEPLOYMENT, QUICKSTART)

### ⏳ Local Testing
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Run test script: `python test_report.py`
- [ ] Start app locally: `streamlit run app.py`
- [ ] Verify app loads at http://localhost:8501
- [ ] Test report generation
- [ ] Verify data displays correctly
- [ ] Test Excel download
- [ ] Check for errors in terminal

### 📝 Code Review
- [ ] Remove any debug code
- [ ] Check for hardcoded paths
- [ ] Verify error handling
- [ ] Review security (API keys)
- [ ] Clean up unused imports
- [ ] Add comments where needed

## Git & GitHub

### 🔧 Prepare Repository
- [ ] Check git status: `git status`
- [ ] Review changes: `git diff`
- [ ] Add files: `git add streamlit_app/`
- [ ] Check what will be committed: `git status`

### 💾 Commit Changes
- [ ] Create commit:
  ```bash
  git commit -m "Add Streamlit self-service report generator

  - Implement Phase 1: Press Premium SVOD Update report
  - Create Streamlit web app with interactive dashboard
  - Add Excel file download functionality
  - Cloud-ready architecture using openpyxl instead of xlwings
  - Add comprehensive documentation"
  ```
- [ ] Verify commit: `git log -1`

### 📤 Push to GitHub
- [ ] Push to remote: `git push origin main`
- [ ] Verify on GitHub web interface
- [ ] Check all files uploaded correctly
- [ ] Verify `streamlit_app/` directory visible

## Streamlit Cloud Deployment

### 🔐 Account Setup
- [ ] Go to https://share.streamlit.io/
- [ ] Sign in with GitHub account
- [ ] Authorize Streamlit to access your repos
- [ ] Verify `AntennaAnalytics/Slide-Production` repo visible

### 🚀 Deploy App
- [ ] Click "New app" button
- [ ] Select repository: `AntennaAnalytics/Slide-Production`
- [ ] Select branch: `main`
- [ ] Set main file path: `streamlit_app/app.py`
- [ ] Choose app URL (subdomain): `antenna-reports` or similar
- [ ] Click "Deploy"

### ⏱️ Monitor Deployment
- [ ] Watch build logs for errors
- [ ] Wait for "Your app is live!" message (~2-5 minutes)
- [ ] Note your app URL: `https://[app-name].streamlit.app`

## Post-Deployment Testing

### 🧪 Smoke Tests
- [ ] Open app URL in browser
- [ ] Verify UI loads correctly
- [ ] Check sidebar navigation
- [ ] Verify report description displays

### 📊 Report Generation Test
- [ ] Click "Press Premium SVOD Update"
- [ ] Click "🚀 Generate Report" button
- [ ] Verify progress spinner appears
- [ ] Wait for completion (~30-60 seconds)
- [ ] Check for errors

### ✅ Verify Output
- [ ] Verify data summary metrics display
- [ ] Check Sign-ups table displays
- [ ] Check Gross Adds table displays
- [ ] Check Churn table displays
- [ ] Verify no error messages

### 📥 Download Test
- [ ] Click "📥 Download Excel Report"
- [ ] Verify file downloads
- [ ] Open Excel file
- [ ] Verify data matches dashboard
- [ ] Check formatting is correct
- [ ] Verify date is current

## Configuration (Optional)

### 🔒 Secrets Management
If moving API keys to secrets:
- [ ] Go to Streamlit Cloud dashboard
- [ ] Click your app
- [ ] Go to Settings → Secrets
- [ ] Add secrets in TOML format:
  ```toml
  [redash]
  signups_api_key = "YOUR_KEY_HERE"
  # ... etc
  ```
- [ ] Save secrets
- [ ] Wait for app to restart
- [ ] Update code to use `st.secrets`
- [ ] Commit and push updated code

### 🎨 Custom Domain (Optional)
If you have a custom domain:
- [ ] Upgrade to Streamlit Team plan
- [ ] Go to app settings
- [ ] Add custom domain
- [ ] Update DNS records
- [ ] Verify SSL certificate

## Documentation & Communication

### 📄 Update Documentation
- [ ] Add actual app URL to documentation
- [ ] Update README with deployment date
- [ ] Add any deployment-specific notes
- [ ] Document any issues encountered

### 📢 Share with Team
- [ ] Prepare announcement message
- [ ] Include app URL
- [ ] Provide quick start instructions
- [ ] Share documentation links
- [ ] Set up support channel (if needed)

### 📧 Example Announcement

```
Subject: New Self-Service Report Generator Now Live!

Hi team,

I'm excited to announce that our new self-service report generator is now live!

🔗 App URL: https://antenna-reports.streamlit.app

📊 Available Reports:
- Press Premium SVOD Update (more coming soon!)

📖 Quick Start:
1. Visit the URL above
2. Click "Press Premium SVOD Update" in the sidebar
3. Click "🚀 Generate Report"
4. View the interactive dashboard
5. Download the Excel file

📚 Documentation:
- Quick Start: [link to QUICKSTART.md]
- Full Guide: [link to README.md]

Questions? Reply to this email or check the documentation.

Happy reporting!
```

## Monitoring & Maintenance

### 📊 Monitor Usage
- [ ] Check Streamlit Cloud dashboard regularly
- [ ] Monitor app logs for errors
- [ ] Review usage statistics
- [ ] Collect user feedback

### 🔄 Updates
When making updates:
- [ ] Test locally first
- [ ] Commit and push to GitHub
- [ ] Verify auto-redeploy completes
- [ ] Test updated app
- [ ] Notify users of changes

### 🐛 Issue Tracking
- [ ] Set up issue tracking (GitHub Issues)
- [ ] Document known issues
- [ ] Track feature requests
- [ ] Prioritize improvements

## Troubleshooting

### ❌ Common Issues Checklist

If deployment fails:
- [ ] Check build logs for specific errors
- [ ] Verify `requirements.txt` is correct
- [ ] Ensure all files are committed
- [ ] Check file paths are correct
- [ ] Verify Python version compatibility

If app won't start:
- [ ] Check for syntax errors
- [ ] Verify imports are available
- [ ] Check file permissions
- [ ] Review Streamlit Cloud logs

If report generation fails:
- [ ] Verify Redash API is accessible
- [ ] Check API keys are valid
- [ ] Verify template file exists
- [ ] Check Output directory is writable
- [ ] Review error messages in logs

## Success Criteria

### ✅ Deployment Successful When:
- [ ] App URL is accessible from any browser
- [ ] UI loads without errors
- [ ] Report generation completes successfully
- [ ] Data displays correctly in dashboard
- [ ] Excel file downloads successfully
- [ ] Excel file contains correct data
- [ ] No errors in Streamlit Cloud logs
- [ ] Team can access and use the app

## Rollback Plan

If critical issues occur:

### Option 1: Quick Fix
- [ ] Identify and fix issue
- [ ] Test locally
- [ ] Commit and push fix
- [ ] Verify auto-redeploy

### Option 2: Rollback
- [ ] In Streamlit Cloud, go to app settings
- [ ] Select previous working deployment
- [ ] Click "Redeploy"
- [ ] Or revert git commit:
  ```bash
  git revert HEAD
  git push origin main
  ```

## Final Verification

### ✅ Final Checks
- [ ] App is live and accessible
- [ ] URL shared with team
- [ ] Documentation is up-to-date
- [ ] Monitoring is in place
- [ ] Support process defined
- [ ] Backup plan documented

### 🎉 Celebration
- [ ] Take a screenshot of live app
- [ ] Document lessons learned
- [ ] Update project status
- [ ] Plan Phase 2

---

## Quick Reference

**App URL**: https://[your-app-name].streamlit.app

**Deployment Command**:
```bash
git add streamlit_app/
git commit -m "Add Streamlit web app"
git push origin main
# Then deploy via https://share.streamlit.io/
```

**Test Command**:
```bash
cd streamlit_app
streamlit run app.py
```

**Log Location**: Streamlit Cloud dashboard → Your App → Manage app → Logs

**Documentation**: `/streamlit_app/README.md`

---

**Status**: Ready for deployment ✅

**Last Updated**: 2026-02-04
