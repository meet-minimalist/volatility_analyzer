'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 12:54:48
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:22:12
 # @ Description: Example usage and entry point
 '''

import logging
from volatility_analyzer import VolatilityAnalyzer


def main():
    """Main entry point demonstrating usage"""
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Initialize analyzer
    analyzer = VolatilityAnalyzer(years_of_data=3)
    
    # # Example 1: Single stock analysis
    # print("="*80)
    # print("EXAMPLE 1: Single Stock Analysis")
    # print("="*80)
    
    # report, stock_data, benchmark_data = analyzer.analyze_stock(
    #     "RELIANCE.NS",
    #     plot_results=False  # Set to True to see plots
    # )
    
    # Example 1.5: Specific Metrics Analysis (New Feature)
    print("\n\n" + "="*80)
    print("EXAMPLE 1.5: Specific Metrics Request")
    print("="*80)
    
    # Ask for specific methods
    results = analyzer.analyze("NVDA", methods=['stddev', 'beta'])
    print(f"Analysis Results for NVDA: {results}")
    
    
    # Example 2: Multiple stock comparison
    print("\n\n" + "="*80)
    print("EXAMPLE 2: Multiple Stock Comparison")
    print("="*80)
    
    # indian_stocks = [
    #     'RELIANCE.NS',
    #     'TCS.NS',
    #     'HDFCBANK.NS',
    #     'INFY.NS',
    #     'ICICIBANK.NS'
    # ]
    
    from config import STOCK_BENCHMARK_MAP
    us_stocks = list(STOCK_BENCHMARK_MAP.keys())
    comparison_df = analyzer.compare_multiple_stocks(
        us_stocks,
        plot_comparison=False  # Set to True to see plots
    )
    
    # # Example 3: Custom benchmark mapping
    # print("\n\n" + "="*80)
    # print("EXAMPLE 3: Custom Benchmark Mapping")
    # print("="*80)
    
    # analyzer.add_benchmark_mapping('AAPL', '^GSPC')
    # report_aapl, _, _ = analyzer.analyze_stock('AAPL', plot_results=False)
    
    # # Example 4: Custom date range
    # print("\n\n" + "="*80)
    # print("EXAMPLE 4: Custom Date Range")
    # print("="*80)
    
    # from datetime import datetime
    # analyzer.set_date_range(
    #     start_date=datetime(2023, 1, 1),
    #     end_date=datetime(2024, 12, 31)
    # )
    # report_custom, _, _ = analyzer.analyze_stock(
    #     "TCS.NS",
    #     plot_results=False
    # )


if __name__ == "__main__":
    main()