# Antenna Analytics - Self-Service Report Generator

A Streamlit web application for generating Antenna Analytics reports on-demand.

## Features

- **Self-Service Reports**: Generate reports with a single click
- **Interactive Dashboards**: View data in interactive tables and charts
- **Downloadable Files**: Download Excel files with formatted reports
- **100% Python**: No JavaScript knowledge required
- **Cloud-Ready**: Designed for Streamlit Community Cloud deployment

## Currently Available Reports

### Phase 1 (Current)
- ✅ **Press Premium SVOD Update**: Monthly premium SVOD metrics for press releases
  - Sign-ups data
  - Gross Adds data
  - Churn data (weighted and monthly)

### Phase 2 (Coming Soon)
- 🚧 Premium SVOD Analytics
- 🚧 BBC Analytics
- 🚧 Gaming Analytics
- 🚧 Sports Analytics
- 🚧 Custom date ranges and filters

## Local Development

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Navigate to the streamlit_app directory:
```bash
cd streamlit_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Configure secrets:
```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml with your actual credentials
```

### Running Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment to Streamlit Community Cloud

### Prerequisites
- GitHub account
- Streamlit Community Cloud account (free at https://share.streamlit.io/)

### Steps

1. **Push to GitHub**:
   - Ensure all changes are committed and pushed to your repository
   - The streamlit_app folder should be in your repo

2. **Deploy to Streamlit Cloud**:
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `AntennaAnalytics/Slide-Production`
   - Set main file path: `streamlit_app/app.py`
   - Click "Deploy"

3. **Configure Secrets** (if needed):
   - In Streamlit Cloud dashboard, go to app settings
   - Add secrets in the "Secrets" section
   - Format: same as `.streamlit/secrets.toml`

4. **Access Your App**:
   - Your app will be available at: `https://[your-app-name].streamlit.app`
   - Example: `https://antenna-reports.streamlit.app`

## Project Structure

```
streamlit_app/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .streamlit/
│   ├── config.toml            # Streamlit configuration
│   └── secrets.toml.example   # Example secrets file
├── reports/
│   ├── __init__.py
│   └── press_update_report.py # Press update report logic
├── utils/
│   └── __init__.py            # Utility functions
└── data/
    └── (Optional data files)
```

## Architecture

### Data Flow
1. User clicks "Generate Report" button
2. App fetches data from Redash API
3. Data is processed and pivoted as needed
4. Interactive dashboard displayed in browser
5. Excel file generated for download

### Key Technologies
- **Streamlit**: Web framework (100% Python)
- **Pandas**: Data manipulation
- **OpenPyXL**: Excel file generation (cloud-compatible)
- **Requests**: API calls to Redash
- **Plotly**: Interactive charts (Phase 2)

## Configuration

### Redash API
Reports fetch data from Redash API endpoints. API keys are embedded in the query definitions (see `reports/press_update_report.py`).

For production deployment, consider moving API keys to Streamlit secrets:

```toml
# .streamlit/secrets.toml
[redash]
signups_api_key = "your_key_here"
gross_adds_api_key = "your_key_here"
# ... etc
```

## Troubleshooting

### Common Issues

**Issue**: "Template file not found"
- **Solution**: Ensure the `templates/` folder exists in the parent directory with the Excel template file

**Issue**: "Module not found" errors
- **Solution**: Verify all dependencies are installed: `pip install -r requirements.txt`

**Issue**: Slow report generation
- **Solution**: Redash queries are cached for 1 hour. First run may be slow, subsequent runs are faster.

**Issue**: Excel file download not working
- **Solution**: Check that the `Output/` folder exists and is writable

## Development Roadmap

### Phase 1: Standard Reports ✅
- [x] Streamlit app structure
- [x] Press Premium SVOD Update report
- [x] Interactive data display
- [x] Excel file download
- [ ] Local testing
- [ ] Deploy to Streamlit Cloud

### Phase 2: Additional Reports
- [ ] Add remaining reports (Premium SVOD, BBC, Gaming, etc.)
- [ ] Refactor report modules for consistency
- [ ] Add error handling and validation

### Phase 3: Custom Parameters
- [ ] Date range picker
- [ ] Service filter (multi-select)
- [ ] Vertical selection
- [ ] Metric customization
- [ ] Comparison mode

### Phase 4: Enhanced Features
- [ ] Interactive Plotly charts
- [ ] Report history/versioning
- [ ] Scheduled reports
- [ ] Email notifications
- [ ] User authentication (if needed)

## Contributing

When adding new reports:

1. Create a new module in `reports/` (e.g., `premium_report.py`)
2. Implement a main function that returns a result dict with:
   - `success`: Boolean
   - `error`: Error message (if any)
   - `data`: DataFrames for display
   - `excel_file`: Path to generated file
3. Import and integrate in `app.py`
4. Update the report catalog in `app.py`

## Support

For questions or issues:
- Create an issue in the GitHub repository
- Contact the Antenna Analytics team

## License

Copyright © 2026 Antenna Analytics. All rights reserved.
