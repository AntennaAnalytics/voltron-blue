# Deployment Guide: Antenna Analytics Web App

This guide walks you through deploying the Antenna Analytics self-service report generator to Streamlit Community Cloud.

## Prerequisites

- [x] Streamlit app created in `/streamlit_app` directory
- [ ] GitHub repository with latest code pushed
- [ ] Streamlit Community Cloud account (free at https://share.streamlit.io/)

## Step-by-Step Deployment

### 1. Test Locally (Optional but Recommended)

Before deploying, test the app locally:

```bash
cd /Users/mcuscagua/Documents/Antenna/Slide-Production/streamlit_app
streamlit run app.py
```

Visit `http://localhost:8501` and verify:
- App loads without errors
- Reports can be generated
- Data displays correctly
- Excel files can be downloaded

### 2. Commit and Push to GitHub

Ensure all changes are committed:

```bash
cd /Users/mcuscagua/Documents/Antenna/Slide-Production

# Check git status
git status

# Add the new streamlit_app directory
git add streamlit_app/

# Commit changes
git commit -m "Add Streamlit self-service report generator

- Implement Phase 1: Press Premium SVOD Update report
- Create Streamlit web app with interactive dashboard
- Add Excel file download functionality
- Cloud-ready architecture using openpyxl instead of xlwings"

# Push to GitHub
git push origin main
```

### 3. Deploy to Streamlit Community Cloud

#### A. Sign Up / Log In

1. Go to https://share.streamlit.io/
2. Click "Sign up" or "Log in"
3. Authenticate with your GitHub account
4. Grant Streamlit access to your repositories

#### B. Create New App

1. Click the **"New app"** button in the top right
2. Fill in the deployment settings:

   - **Repository**: Select `AntennaAnalytics/Slide-Production`
   - **Branch**: `main` (or your working branch)
   - **Main file path**: `streamlit_app/app.py`
   - **App URL** (optional): Choose a custom subdomain like `antenna-reports`

3. Click **"Deploy"**

#### C. Wait for Deployment

- Initial deployment takes 2-5 minutes
- You'll see build logs in real-time
- Once complete, your app will be live at:
  ```
  https://[your-app-name].streamlit.app
  ```

### 4. Configure Secrets (If Needed)

Currently, API keys are embedded in the code. For production, you may want to move them to Streamlit secrets:

1. In Streamlit Cloud dashboard, click your app
2. Click **"Settings"** (⚙️ icon)
3. Navigate to **"Secrets"**
4. Add secrets in TOML format:

```toml
# Example - not currently used but ready for Phase 2
[redash]
base_url = "https://redash.uuid-p.antennaanalytics.com"
signups_api_key = "QSTJ3AfkTmgvLmnlKPuLeSlSeYE36BBnTvjAMR7J"
gross_adds_api_key = "D7fcPON9HY9lfy9fcvU6oldWwHf65n1UYSCk1RWX"
churn_weighted_api_key = "x8y07f11DW84Wf2aMExLBF0HWY2Ng12RCY6w4XEL"
churn_monthly_api_key = "WN7YMBY9xvC2SQnRPTIQpIu4EmCRYgwtXLcYg4a1"
```

5. Click **"Save"**
6. App will automatically restart with new secrets

To use secrets in code (for Phase 2):

```python
import streamlit as st

# Access secrets
api_key = st.secrets["redash"]["signups_api_key"]
```

### 5. Verify Deployment

Once deployed, test the app:

1. Visit your app URL: `https://[your-app-name].streamlit.app`
2. Verify the UI loads correctly
3. Generate a test report:
   - Click **"Press Premium SVOD Update"** in sidebar
   - Click **"🚀 Generate Report"**
   - Wait for report generation (30-60 seconds)
   - Verify data tables display
   - Download Excel file and verify contents

### 6. Share with Users

Share the URL with your team:

```
https://antenna-reports.streamlit.app
```

Users can:
- Bookmark the URL
- Generate reports on-demand
- Download Excel files
- View interactive dashboards

## Updating the App

When you make changes to the code:

1. **Commit and push changes**:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```

2. **Automatic redeployment**:
   - Streamlit Cloud watches your GitHub repo
   - Automatically redeploys when you push to `main`
   - Takes 1-2 minutes to update

3. **Manual redeployment** (if needed):
   - Go to Streamlit Cloud dashboard
   - Click your app
   - Click "Reboot" button

## Troubleshooting

### App Won't Start

**Issue**: App crashes on startup

**Solutions**:
- Check build logs in Streamlit Cloud dashboard
- Verify `requirements.txt` has all dependencies
- Ensure Python version compatibility (Python 3.8+)
- Check for syntax errors in code

### Template File Not Found

**Issue**: Error: "Template file not found"

**Solutions**:
- Verify `templates/` folder exists in parent directory
- Ensure `Antenna for Press_PremiumSVOD_ yyyymmdd.xlsx` exists in templates
- Check file paths are correct (relative paths may differ in cloud)

**Fix**: Update template path in `reports/press_update_report.py`:

```python
template_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "templates",
    "Antenna for Press_PremiumSVOD_ yyyymmdd.xlsx"
)
```

### Report Generation Slow

**Issue**: Report takes >60 seconds to generate

**Solutions**:
- Check Redash API response times
- Enable caching (already implemented via `@st.cache_data`)
- Consider optimizing queries in Redash
- Monitor Streamlit Cloud resource usage

### Excel File Download Fails

**Issue**: Download button doesn't work

**Solutions**:
- Verify output file is created successfully
- Check file permissions
- Ensure file path is accessible
- Try clearing browser cache

### API Request Failures

**Issue**: "Error fetching data" messages

**Solutions**:
- Verify Redash API is accessible from cloud
- Check API keys are valid
- Ensure query IDs are correct
- Verify network connectivity

## Monitoring & Maintenance

### View Logs

1. Go to Streamlit Cloud dashboard
2. Click your app
3. Click "Manage app" → "Logs"
4. View real-time application logs

### Monitor Usage

Streamlit Community Cloud (free tier):
- **Monthly viewers**: Unlimited
- **Resources**: Shared CPU/memory
- **Data transfer**: 1 GB/month

For higher usage, consider:
- **Streamlit Cloud Team** ($20/month per editor)
- **Streamlit Cloud Enterprise** (custom pricing)

### Update Dependencies

To update Python packages:

1. Edit `requirements.txt`
2. Update version numbers
3. Commit and push:
   ```bash
   git add streamlit_app/requirements.txt
   git commit -m "Update: upgrade package versions"
   git push origin main
   ```

## Next Steps

### Phase 2: Add More Reports

1. Refactor additional report scripts (Premium SVOD, BBC, Gaming, etc.)
2. Create new modules in `streamlit_app/reports/`
3. Add report entries to `app.py` catalog
4. Test locally, then deploy

### Phase 3: Custom Parameters

1. Add Streamlit input widgets (date pickers, multi-selects)
2. Update report functions to accept parameters
3. Implement filtering and customization logic
4. Deploy and test

### Phase 4: Advanced Features

- Interactive Plotly charts
- Report scheduling
- User authentication (if needed)
- Email notifications
- API rate limiting
- Error reporting/monitoring

## Support

For issues or questions:
- Check Streamlit documentation: https://docs.streamlit.io/
- Streamlit Community Forum: https://discuss.streamlit.io/
- GitHub Issues: Create an issue in the repo

## Security Notes

### API Keys

- Currently, API keys are in the code (acceptable for internal tools)
- For production, move to Streamlit secrets
- Rotate keys periodically
- Never commit secrets to git

### Access Control

Streamlit Community Cloud apps are **public by default**:
- Anyone with the URL can access the app
- No built-in authentication on free tier

For restricted access:
- Upgrade to Team or Enterprise plan (includes auth)
- Or implement custom authentication
- Or use firewall/VPN restrictions

## Costs

### Current: Free Tier
- **Cost**: $0/month
- **Limits**: Unlimited viewers, shared resources
- **Suitable for**: Internal tools, prototypes

### Optional: Team Plan
- **Cost**: $20/month per editor
- **Features**: Private apps, authentication, priority support
- **Suitable for**: Production apps with restricted access

## Rollback

If deployment fails or has issues:

1. **Revert to previous commit**:
   ```bash
   git revert HEAD
   git push origin main
   ```

2. **Or rollback in Streamlit Cloud**:
   - Go to app settings
   - Select previous deployment
   - Click "Redeploy"

---

**Deployment Checklist**

- [ ] Local testing completed
- [ ] Changes committed to git
- [ ] Pushed to GitHub main branch
- [ ] Streamlit Cloud account created
- [ ] App deployed successfully
- [ ] Test report generation works
- [ ] Excel download works
- [ ] URL shared with team
- [ ] Documentation updated

**Your App URL**: `https://[your-app-name].streamlit.app`

🎉 **Congratulations! Your Antenna Analytics web app is live!**
