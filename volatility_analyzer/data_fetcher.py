'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 14:27:36
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:20:50
 # @ Description: Data fetching and caching logic
 '''

import yfinance as yf
import pandas as pd
from datetime import datetime
from typing import Tuple, Optional
from yf_cache import YFinanceDataDownloader

from logging_config import get_logger

logger = get_logger(__name__)

class DataFetcher:
    """Fetches stock and benchmark data with caching"""
    
    def __init__(self, cache_dir: str = "yfinance_data"):
        """
        Initialize data fetcher
        
        Args:
            cache_dir: Directory for caching data
        """
        self.downloader = YFinanceDataDownloader(cache_dir=cache_dir, log_level="ERROR")
    
    def fetch_stock_data(
        self, 
        ticker: str, 
        start_date: datetime, 
        end_date: datetime
    ) -> pd.DataFrame:
        """
        Fetch stock data with caching
        
        Args:
            ticker: Stock ticker symbol
            start_date: Start date for data
            end_date: End date for data
            
        Returns:
            DataFrame with stock price data
        """
        return self.downloader.get_data(ticker, start_date, end_date, interval="1d")
    
    def fetch_benchmark_data(
        self,
        benchmark_ticker: str,
        start_date: datetime,
        end_date: datetime
    ) -> Tuple[pd.DataFrame, str]:
        """
        Fetch benchmark data with fallback support
        
        Args:
            benchmark_ticker: Benchmark ticker symbol
            start_date: Start date for data
            end_date: End date for data
            
        Returns:
            Tuple of (DataFrame with benchmark data, actual ticker used)
        """
        try:
            data = self.downloader.get_data(
                benchmark_ticker, start_date, end_date, interval="1d"
            )
            
            if data.empty:
                raise ValueError("Empty benchmark data")
            
            return data, benchmark_ticker
            
        except Exception as e:
            logger.warning(f"Could not download {benchmark_ticker}: {e}")
            
            # Final fallback to Nifty 50
            logger.warning("Using Nifty 50 as final fallback")
            data = self.downloader.get_data(
                '^NSEI', start_date, end_date, interval="1d"
            )
            return data, '^NSEI'
    
    def get_stock_name(self, ticker: str) -> str:
        """Get stock long name from yfinance"""
        try:
            info = yf.Ticker(ticker)
            return info.info.get('longName', ticker)
        except:
            return ticker
    
    def clear_cache(self, ticker: Optional[str] = None):
        """Clear cached data"""
        self.downloader.clear_cache(ticker)
