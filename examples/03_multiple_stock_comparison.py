'''
 # @ Author: Meet Patel
 # @ Create Time: 2026-01-01 14:18:30
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 14:19:25
 # @ Description:
 '''

'''
Example 3: Multiple Stock Comparison
'''

import logging

from volatility_analyzer import VolatilityAnalyzer
from volatility_analyzer.config import STOCK_BENCHMARK_MAP

def run_example():
    logging.basicConfig(level=logging.INFO)
    analyzer = VolatilityAnalyzer(years_of_data=3)
    
    print("\n\n" + "="*80)
    print("EXAMPLE 2: Multiple Stock Comparison")
    print("="*80)
    
    # Use stocks defined in config
    us_stocks = list(STOCK_BENCHMARK_MAP.keys())
    
    comparison_df = analyzer.compare_multiple_stocks(
        us_stocks,
        plot_comparison=True
    )

if __name__ == "__main__":
    run_example()