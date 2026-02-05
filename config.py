"""
Configuration file for Antenna Analytics Report Generator
Contains metadata and configuration for all reports
"""

# Report catalog with detailed metadata
REPORTS_CATALOG = {
    "press_premium_svod": {
        "name": "Press Premium SVOD Update",
        "category": "Press & Updates",
        "description": "Monthly premium SVOD metrics for press releases",
        "details": """
This report generates comprehensive **Premium SVOD metrics** designed for press releases and external communications.

**Data Included:**
- **Sign-ups**: Monthly sign-up trends across major streaming services
- **Gross Adds**: Monthly gross subscriber additions by service
- **Churn Metrics**: Weighted and unweighted monthly churn rates

**Output Formats:**
- Interactive dashboard with sortable tables
- Downloadable Excel file with formatted data
- Pre-configured template with company branding

**Update Frequency:** Monthly
**Data Sources:** Redash queries (20491, 20492, 20493, 20494)
**Processing Time:** ~30-60 seconds
        """,
        "available": True,
        "queries": [20491, 20492, 20493, 20494],
        "output_format": "Excel (.xlsx)",
        "estimated_time": "30-60 seconds"
    },
    "premium_svod": {
        "name": "Premium SVOD Analytics",
        "category": "Premium SVOD",
        "description": "Comprehensive premium SVOD subscriber analytics",
        "details": """
Coming soon: Detailed analytics for premium SVOD services including subscriber trends,
demographics, engagement metrics, and competitive analysis.
        """,
        "available": False,
        "output_format": "Excel (.xlsx)",
        "estimated_time": "TBD"
    },
    "bbc": {
        "name": "BBC Analytics",
        "category": "Vertical Reports",
        "description": "BBC-specific subscriber analytics and insights",
        "details": """
Coming soon: Specialized analytics for BBC streaming services.
        """,
        "available": False,
        "output_format": "Excel (.xlsx)",
        "estimated_time": "TBD"
    },
    "gaming": {
        "name": "Gaming Analytics",
        "category": "Vertical Reports",
        "description": "Gaming platform subscriber analytics",
        "details": """
Coming soon: Analytics for gaming subscription platforms and services.
        """,
        "available": False,
        "output_format": "Excel (.xlsx)",
        "estimated_time": "TBD"
    },
    "sports": {
        "name": "Sports Analytics",
        "category": "Vertical Reports",
        "description": "Sports streaming subscriber analytics",
        "details": """
Coming soon: Specialized analytics for sports streaming services.
        """,
        "available": False,
        "output_format": "Excel (.xlsx)",
        "estimated_time": "TBD"
    }
}

# App configuration
APP_CONFIG = {
    "title": "Antenna Analytics",
    "subtitle": "Self-Service Report Generator",
    "page_icon": "📊",
    "layout": "wide",
    "theme": {
        "primary_color": "#1f77b4",
        "secondary_color": "#ff7f0e",
        "background_color": "#ffffff",
        "text_color": "#262730"
    }
}

# Navigation tabs
NAV_TABS = ["Standard Reports", "Query Pulls", "Documentation"]
