"""
Quick test script to validate the press update report generation
without running the full Streamlit app
"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reports.press_update_report import generate_press_update_report

def test_report_generation():
    """Test the report generation function"""
    print("Testing Press Premium SVOD Update Report Generation...")
    print("=" * 60)

    try:
        result = generate_press_update_report()

        print(f"\nSuccess: {result['success']}")

        if result['success']:
            print(f"Report Date: {result['report_date']}")
            print(f"\nData Summary:")
            print(f"  - Sign-ups rows: {result['data_summary']['signups_rows']}")
            print(f"  - Gross Adds rows: {result['data_summary']['gross_adds_rows']}")
            print(f"  - Churn rows: {result['data_summary']['churn_rows']}")

            if result['excel_file']:
                print(f"\nExcel file generated: {result['excel_file']}")
                print(f"File exists: {os.path.exists(result['excel_file'])}")

            # Display sample data
            if result['data']['signups'] is not None:
                print(f"\nSign-ups Data Preview:")
                print(result['data']['signups'].head())

        else:
            print(f"\nError: {result.get('error')}")
            if result.get('details'):
                print(f"Details: {result.get('details')}")

    except Exception as e:
        print(f"\nException occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_report_generation()
