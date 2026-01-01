"""
# @ Author: Meet Patel
# @ Create Time: 2026-01-01 14:18:34
# @ Modified by: Meet Patel
# @ Modified time: 2026-01-01 14:19:34
# @ Description:
"""

"""
Example 4: Custom Benchmark Mapping
"""

import logging
from volatility_analyzer import VolatilityAnalyzer


def run_example():
    logging.basicConfig(level=logging.INFO)
    analyzer = VolatilityAnalyzer(years_of_data=3)

    print("\n\n" + "=" * 80)
    print("EXAMPLE 3: Custom Benchmark Mapping")
    print("=" * 80)

    report_aapl, _, _ = analyzer.analyze_stock("AAPL", "^GSPC", plot_results=True)


if __name__ == "__main__":
    run_example()
