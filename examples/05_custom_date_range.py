'''
 # @ Author: Meet Patel
 # @ Create Time: 2026-01-01 14:18:36
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 14:19:41
 # @ Description:
 '''

'''
Example 5: Custom Date Range
'''

import logging
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from volatility_analyzer import VolatilityAnalyzer

def run_example():
    logging.basicConfig(level=logging.INFO)
    analyzer = VolatilityAnalyzer(years_of_data=3)
    
    print("\n\n" + "="*80)
    print("EXAMPLE 4: Custom Date Range")
    print("="*80)
    
    analyzer.set_date_range(
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2024, 12, 31)
    )
    report_custom, _, _ = analyzer.analyze_stock("TCS.NS", plot_results=True)

if __name__ == "__main__":
    run_example()