"""
# @ Author: Meet Patel
# @ Create Time: 2026-01-01 14:18:30
# @ Modified by: Meet Patel
# @ Modified time: 2026-01-01 14:19:25
# @ Description:
"""

"""
Example 2: Multiple Stock Comparison
"""

import logging
from volatility_analyzer import VolatilityAnalyzer


def run_example():
    logging.basicConfig(level=logging.INFO)
    analyzer = VolatilityAnalyzer(years_of_data=3)

    print("\n\n" + "=" * 80)
    print("EXAMPLE 2: Multiple Stock Comparison")
    print("=" * 80)

    # ========== INDIAN STOCKS (for reference) ==========
    stock_dict = {
        "RELIANCE.NS": "^NSEI",
        "TCS.NS": "^NSEI",
        "HDFCBANK.NS": "^NSEI",
        "INFY.NS": "^NSEI",
        "HINDUNILVR.NS": "^NSEI",
        "ICICIBANK.NS": "^NSEI",
        "KOTAKBANK.NS": "^NSEI",
        "SBIN.NS": "^NSEI",
        "BHARTIARTL.NS": "^NSEI",
        "ITC.NS": "^NSEI",
    }

    comparison_df = analyzer.compare_multiple_stocks(stock_dict, plot_comparison=True)


if __name__ == "__main__":
    run_example()
