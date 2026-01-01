'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 14:28:52
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:23:13
 # @ Description: Main volatility analyzer orchestrating all components
 '''

from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
import pandas as pd

from volatility_analyzer.config import (
    DEFAULT_YEARS_OF_DATA,
    DEFAULT_CACHE_DIR,
    DEFAULT_ROLLING_VOLATILITY_WINDOW,
    DEFAULT_ROLLING_BETA_WINDOW
)
# from benchmark_selector import BenchmarkSelector
from volatility_analyzer.data_fetcher import DataFetcher
from volatility_analyzer.metrics_calculator import MetricsCalculator
from volatility_analyzer.visualization import AnalysisVisualizer
from volatility_analyzer.data_models import AnalysisReport


class VolatilityAnalyzer:
    """
    Main analyzer for stock volatility and beta analysis.
    Orchestrates all components following single responsibility principle.
    """
    
    def __init__(
        self,
        years_of_data: int = DEFAULT_YEARS_OF_DATA,
        cache_dir: str = DEFAULT_CACHE_DIR,
    ):
        """
        Initialize the volatility analyzer
        
        Args:
            years_of_data: Number of years of historical data
            cache_dir: Directory for caching downloaded data
        """
        self.years_of_data = years_of_data
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=365 * years_of_data)
        
        # Initialize components
        self.data_fetcher = DataFetcher(cache_dir)
        self.metrics_calculator = MetricsCalculator()
        self.visualizer = AnalysisVisualizer()
    
    def analyze_stock(
        self,
        ticker: str,
        benchmark_ticker: str,
        plot_results: bool = True
    ) -> Tuple[AnalysisReport, pd.DataFrame, pd.DataFrame]:
        """
        Perform complete volatility and beta analysis for a stock
        
        Args:
            ticker: Stock ticker symbol
            benchmark_ticker: Benchmark ticker (required)
            plot_results: Whether to create visualization plots
            
        Returns:
            Tuple of (AnalysisReport, stock_data, benchmark_data)
        """
        # Step 1: Select benchmark
        if benchmark_ticker is None:
            raise RuntimeError("Benchmark stock not provided.")
        
        print(f"\nAnalyzing {ticker} vs {benchmark_ticker}")
        print(f"Period: {self.start_date.date()} to {self.end_date.date()}")
        
        # Step 2: Fetch data
        stock_data = self.data_fetcher.fetch_stock_data(
            ticker, self.start_date, self.end_date
        )
        benchmark_data, actual_benchmark = self.data_fetcher.fetch_benchmark_data(
            benchmark_ticker, self.start_date, self.end_date
        )
        
        # Get names
        stock_name = self.data_fetcher.get_stock_name(ticker)
        benchmark_name = self.data_fetcher.get_stock_name(actual_benchmark)
        
        print(f"Stock: {stock_name}")
        print(f"Benchmark: {benchmark_name}")
        
        # Step 3: Calculate returns
        stock_returns = self.metrics_calculator.calculate_returns(stock_data)
        benchmark_returns = self.metrics_calculator.calculate_returns(benchmark_data)
        
        # Step 4: Calculate metrics
        stock_metrics = self.metrics_calculator.calculate_stock_metrics(
            ticker, stock_name, stock_returns
        )
        benchmark_metrics = self.metrics_calculator.calculate_benchmark_metrics(
            actual_benchmark, benchmark_name, benchmark_returns
        )
        beta_analysis = self.metrics_calculator.calculate_beta(
            stock_returns, benchmark_returns
        )
        
        # Step 5: Calculate rolling metrics
        rolling_vol = self.metrics_calculator.calculate_rolling_volatility(
            stock_returns, window_days=DEFAULT_ROLLING_VOLATILITY_WINDOW
        )
        rolling_metrics = self.metrics_calculator.calculate_rolling_beta(
            stock_returns, benchmark_returns, window_days=DEFAULT_ROLLING_BETA_WINDOW
        )
        
        # Step 6: Create analysis report
        report = AnalysisReport(
            stock_metrics=stock_metrics,
            benchmark_metrics=benchmark_metrics,
            beta_analysis=beta_analysis,
            period_start=str(self.start_date.date()),
            period_end=str(self.end_date.date()),
            data_points=len(beta_analysis.aligned_data),
            volatility_ratio=stock_metrics.volatility_annual / benchmark_metrics.volatility_annual,
            rolling_volatility=rolling_vol,
            rolling_metrics=rolling_metrics
        )
        
        # Step 7: Log report
        report.log_report()
        
        # Step 8: Visualize if requested
        if plot_results:
            self.visualizer.plot_single_stock_analysis(
                report, stock_data, benchmark_data,
                stock_returns, benchmark_returns
            )
        
        return report, stock_data, benchmark_data
    
    def compare_multiple_stocks(
        self,
        ticker_dict: Dict[str, str],
        plot_comparison: bool = True
    ) -> Optional[pd.DataFrame]:
        """
        Compare multiple stocks against their respective benchmarks
        
        Args:
            ticker_dict: Dictionary mapping stock ticker symbols to their benchmark ticker symbols
            plot_comparison: Whether to create comparison plots
            
        Returns:
            DataFrame with comparison results
        """
        results_list = []
        
        print(f"\nComparing {len(ticker_dict)} stocks...")
        print("-" * 80)
        
        for ticker, benchmark in ticker_dict.items():
            print(f"\nAnalyzing {ticker}...")
            try:
                report, _, _ = self.analyze_stock(ticker, benchmark_ticker=benchmark, plot_results=False)
                results_list.append(report.to_dict())
            except Exception as e:
                print(f"Error analyzing {ticker}: {e}")
                continue
        
        if not results_list:
            print("No results to compare")
            return None
        
        # Create comparison dataframe
        df = pd.DataFrame(results_list)
        comparison_cols = [
            'Stock', 'Ticker', 'Benchmark',
            'Stock_Volatility_Annual', 'Benchmark_Volatility_Annual',
            'Beta', 'R_Squared', 'Volatility_Ratio'
        ]
        comparison_df = df[comparison_cols].copy()
        
        # Convert volatility to float for sorting
        comparison_df['Volatility_Pct'] = (
            comparison_df['Stock_Volatility_Annual']
            .str.rstrip('%')
            .astype(float)
        )
        comparison_df = comparison_df.sort_values('Volatility_Pct', ascending=False)
        
        # Print comparison summary
        print("\n" + "="*80)
        print("STOCK COMPARISON SUMMARY")
        print("="*80)
        print(comparison_df.to_string(index=False))
        
        # Visualize comparison
        if plot_comparison and len(comparison_df) > 1:
            self.visualizer.plot_comparison(comparison_df)
        
        return comparison_df
    
    def clear_cache(self, ticker: Optional[str] = None):
        """
        Clear cached data
        
        Args:
            ticker: Specific ticker to clear (None = clear all)
        """
        self.data_fetcher.clear_cache(ticker)
    
    def set_date_range(self, start_date: datetime, end_date: datetime):
        """Set custom date range for analysis"""
        self.start_date = start_date
        self.end_date = end_date
