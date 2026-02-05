"""
Antenna Analytics - Self-Service Report Generator
Main Streamlit application for generating reports on-demand
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Add the parent directory to path to import from reports module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reports.press_update_report import generate_press_update_report
from config import REPORTS_CATALOG, APP_CONFIG, NAV_TABS

# Page configuration
st.set_page_config(
    page_title=f"{APP_CONFIG['title']} - Report Generator",
    page_icon=APP_CONFIG['page_icon'],
    layout=APP_CONFIG['layout'],
    initial_sidebar_state="expanded"
)

# Custom CSS for cleaner, more professional styling
st.markdown("""
    <style>
    /* Reduce overall font sizes */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Header styling */
    .app-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1f77b4;
        margin-bottom: 0.2rem;
    }

    .app-subtitle {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1.5rem;
    }

    /* Report preview card */
    .report-preview {
        background-color: #f8f9fa;
        border-left: 4px solid #1f77b4;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }

    .report-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #262730;
        margin-bottom: 0.5rem;
    }

    .report-description {
        font-size: 0.9rem;
        color: #555;
        line-height: 1.5;
    }

    /* Metrics styling */
    [data-testid="stMetricValue"] {
        font-size: 1.2rem;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.85rem;
    }

    /* Button styling */
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-weight: 500;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 0.3rem;
        font-size: 0.95rem;
    }

    .stButton>button:hover {
        background-color: #145a8c;
    }

    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #ffffff;
        border-bottom: 2px solid #e0e0e0;
        padding: 0.5rem 0;
    }

    .stTabs [data-baseweb="tab"] {
        font-size: 0.95rem;
        font-weight: 500;
        padding: 0.5rem 1rem;
        color: #666;
    }

    .stTabs [aria-selected="true"] {
        color: #1f77b4;
        border-bottom: 3px solid #1f77b4;
    }

    /* Table styling */
    .dataframe {
        font-size: 0.85rem !important;
    }

    /* Reduce header sizes in content */
    h1 {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
    }

    h2 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
    }

    h3 {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    h4 {
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }

    /* Info/warning boxes */
    .stAlert {
        font-size: 0.9rem;
        padding: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown(f'<div class="app-header">{APP_CONFIG["page_icon"]} {APP_CONFIG["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="app-subtitle">{APP_CONFIG["subtitle"]}</div>', unsafe_allow_html=True)

# Top navigation tabs
tab1, tab2, tab3 = st.tabs(NAV_TABS)

# ============================================================================
# TAB 1: STANDARD REPORTS
# ============================================================================
with tab1:
    # Sidebar for report selection (only in Standard Reports tab)
    with st.sidebar:
        st.markdown("### Report Selection")

        # Get available reports
        available_reports = {k: v for k, v in REPORTS_CATALOG.items() if v.get("available", False)}

        # Create dropdown options
        report_options = {
            f"{report['name']}": report_key
            for report_key, report in available_reports.items()
        }

        # Dropdown for report selection
        selected_report_name = st.selectbox(
            "Choose a report:",
            options=list(report_options.keys()),
            help="Select a report to view details and generate"
        )

        selected_report_key = report_options[selected_report_name]
        selected_report = REPORTS_CATALOG[selected_report_key]

        st.markdown("---")

        # Report metadata in sidebar
        st.markdown("#### Report Details")
        st.markdown(f"**Category:** {selected_report['category']}")
        st.markdown(f"**Format:** {selected_report.get('output_format', 'N/A')}")
        st.markdown(f"**Est. Time:** {selected_report.get('estimated_time', 'N/A')}")

        if selected_report.get('queries'):
            st.markdown(f"**Queries:** {len(selected_report['queries'])}")

    # Main content area
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown(f"## {selected_report['name']}")
        st.markdown(f"*{selected_report['description']}*")

        # Report details
        st.markdown("### Overview")
        st.markdown(selected_report['details'])

    with col_right:
        # Quick actions panel
        st.markdown("### Quick Actions")

        # Generate report button
        if st.button("🚀 Generate Report", key="generate_report", use_container_width=True):
            generate_report_flag = True
        else:
            generate_report_flag = False

        st.markdown("---")

        # Report info box
        st.info(
            f"This report will generate the latest data from {len(selected_report.get('queries', []))} "
            f"data sources and provide both an interactive dashboard and downloadable Excel file."
        )

    # Report generation section
    if generate_report_flag and selected_report_key == "press_premium_svod":
        st.markdown("---")

        with st.spinner(f"⏳ Generating report... This may take {selected_report['estimated_time']}"):
            try:
                # Call the report generation function
                result = generate_press_update_report()

                if result["success"]:
                    st.success("✅ Report generated successfully!")

                    # Display data summary with metrics
                    st.markdown("### 📊 Data Summary")

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Sign-ups Rows", result["data_summary"]["signups_rows"])
                    with col2:
                        st.metric("Gross Adds Rows", result["data_summary"]["gross_adds_rows"])
                    with col3:
                        st.metric("Churn Rows", result["data_summary"]["churn_rows"])
                    with col4:
                        st.metric("Report Date", result["report_date"])

                    # Tabbed data view
                    st.markdown("### 📈 Data Tables")

                    data_tab1, data_tab2, data_tab3 = st.tabs(["Sign-ups", "Gross Adds", "Churn"])

                    with data_tab1:
                        if result["data"]["signups"] is not None and not result["data"]["signups"].empty:
                            st.dataframe(
                                result["data"]["signups"],
                                use_container_width=True,
                                height=400
                            )
                        else:
                            st.info("No sign-ups data available")

                    with data_tab2:
                        if result["data"]["gross_adds"] is not None and not result["data"]["gross_adds"].empty:
                            st.dataframe(
                                result["data"]["gross_adds"],
                                use_container_width=True,
                                height=400
                            )
                        else:
                            st.info("No gross adds data available")

                    with data_tab3:
                        if result["data"]["churn"] is not None and not result["data"]["churn"].empty:
                            st.dataframe(
                                result["data"]["churn"],
                                use_container_width=True,
                                height=400
                            )
                        else:
                            st.info("No churn data available")

                    # Download section
                    st.markdown("---")
                    st.markdown("### 📥 Download Report")

                    col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
                    with col_dl2:
                        if result["excel_file"]:
                            with open(result["excel_file"], "rb") as file:
                                st.download_button(
                                    label="📥 Download Excel Report",
                                    data=file,
                                    file_name=os.path.basename(result["excel_file"]),
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                    use_container_width=True
                                )

                else:
                    st.error(f"❌ Error: {result.get('error', 'Unknown error')}")
                    if result.get("details"):
                        with st.expander("Error Details"):
                            st.error(result['details'])

            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")
                with st.expander("Full Error Details"):
                    st.exception(e)

# ============================================================================
# TAB 2: QUERY PULLS
# ============================================================================
with tab2:
    # Full width layout for Query Pulls (no sidebar)
    st.markdown("## Query Pulls")
    st.info("🚧 Coming soon: Direct query execution and custom data pulls")

    # Two column layout for Query Pulls section
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Features
        - Execute custom Redash queries
        - Pull specific datasets on-demand
        - Export raw data in various formats
        - Schedule recurring data pulls
        """)

    with col2:
        st.markdown("""
        ### Coming Soon
        - Query builder interface
        - Custom parameter inputs
        - Multiple export formats (CSV, JSON, Parquet)
        - Query scheduling
        """)

# ============================================================================
# TAB 3: DOCUMENTATION
# ============================================================================
with tab3:
    # Full width layout for Documentation (no sidebar)
    st.markdown("## Documentation")

    doc_section = st.selectbox(
        "Select documentation section:",
        ["Getting Started", "Available Reports", "FAQ", "API Reference"]
    )

    if doc_section == "Getting Started":
        st.markdown("""
        ### Getting Started with Antenna Analytics

        Welcome to the Antenna Analytics Self-Service Report Generator. This application
        allows you to generate comprehensive analytics reports on-demand.

        #### How to Use

        1. **Navigate to Standard Reports** tab
        2. **Select a report** from the dropdown menu
        3. **Review report details** in the main panel
        4. **Click "Generate Report"** to create the latest version
        5. **View results** in the interactive dashboard
        6. **Download** the Excel file when ready

        #### Tips

        - Reports are cached for 1 hour to improve performance
        - Generation typically takes 30-60 seconds
        - Excel files are date-stamped automatically
        - All data is pulled from Redash in real-time
        """)

    elif doc_section == "Available Reports":
        st.markdown("### Available Reports")

        for report_key, report in REPORTS_CATALOG.items():
            status = "✅ Available" if report.get("available", False) else "🚧 Coming Soon"

            with st.expander(f"{report['name']} - {status}"):
                st.markdown(f"**Category:** {report['category']}")
                st.markdown(f"**Description:** {report['description']}")
                if report.get('queries'):
                    st.markdown(f"**Data Sources:** {len(report['queries'])} queries")
                st.markdown(report['details'])

    elif doc_section == "FAQ":
        st.markdown("""
        ### Frequently Asked Questions

        **Q: How often is the data updated?**
        A: Data is pulled directly from Redash in real-time when you generate a report.

        **Q: Can I schedule reports to run automatically?**
        A: Not yet, but this feature is planned for a future release.

        **Q: What file formats are supported?**
        A: Currently, reports are generated in Excel (.xlsx) format.

        **Q: How long are reports cached?**
        A: Report data is cached for 1 hour to improve performance.

        **Q: Can I customize report parameters?**
        A: Custom parameters are planned for Phase 3 of development.
        """)

    elif doc_section == "API Reference":
        st.markdown("""
        ### API Reference

        🚧 API documentation coming soon.

        This section will include:
        - REST API endpoints
        - Authentication methods
        - Request/response formats
        - Code examples
        """)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #999; font-size: 0.8rem;">'
    f'{APP_CONFIG["title"]} © 2026 | Powered by Streamlit'
    '</div>',
    unsafe_allow_html=True
)
