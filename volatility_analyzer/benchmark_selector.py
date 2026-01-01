'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 14:27:07
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:20:34
 # @ Description: Logic for selecting appropriate benchmarks
 '''

from typing import Optional
from config import STOCK_BENCHMARK_MAP


class BenchmarkSelector:
    """Selects appropriate benchmark index for a given stock"""
    
    def __init__(self, custom_mappings: Optional[dict] = None):
        """
        Initialize benchmark selector
        
        Args:
            custom_mappings: Optional custom stock-to-benchmark mappings
        """
        self.mappings = STOCK_BENCHMARK_MAP.copy()
        if custom_mappings:
            self.mappings.update(custom_mappings)
    
    def get_benchmark(self, ticker: str) -> str:
        """
        Get appropriate benchmark for a given stock ticker
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Benchmark ticker symbol
        """
        # Check explicit mapping first
        if ticker in self.mappings:
            return self.mappings[ticker]
        
        # Infer from ticker suffix
        if ticker.endswith('.NS'):
            return '^NSEI'  # Nifty 50 for NSE stocks
        elif ticker.endswith('.BO'):
            return '^BSESN'  # Sensex for BSE stocks
        else:
            return '^GSPC'  # S&P 500 as default
    
    def add_mapping(self, ticker: str, benchmark: str):
        """Add or update a stock-to-benchmark mapping"""
        self.mappings[ticker] = benchmark
    
    def remove_mapping(self, ticker: str):
        """Remove a custom mapping"""
        if ticker in self.mappings:
            del self.mappings[ticker]
