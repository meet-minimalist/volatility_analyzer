'''
 # @ Author: Meet Patel
 # @ Create Time: 2026-01-01 14:18:01
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 14:19:09
 # @ Description:
 '''

'''
Example 1: Single Stock Analysis
'''

import logging
from volatility_analyzer import VolatilityAnalyzer

def run_example():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    analyzer = VolatilityAnalyzer(years_of_data=3)
    
    print("="*80)
    print("EXAMPLE 1: Single Stock Analysis")
    print("="*80)
    
    report, stock_data, benchmark_data = analyzer.analyze_stock(
        "RELIANCE.NS",
        "^NSEI",
        plot_results=True
    )

if __name__ == "__main__":
    run_example()