"""
# @ Author: Meet Patel
# @ Create Time: 2025-12-28 14:27:59
# @ Modified by: Meet Patel
# @ Modified time: 2026-01-01 13:22:32
# @ Description: Calculate volatility, beta, and other financial metrics
"""

import pandas as pd
import numpy as np
from typing import Tuple
from volatility_analyzer.config import TRADING_DAYS_PER_YEAR
from volatility_analyzer.data_models import (
    StockMetrics,
    BenchmarkMetrics,
    BetaAnalysisResult,
)


class MetricsCalculator:
    """Calculate financial metrics from price and return data"""

    @staticmethod
    def calculate_returns(price_data: pd.DataFrame) -> pd.Series:
        """
        Calculate daily returns from price data

        Args:
            price_data: DataFrame with 'Close' prices

        Returns:
            Series of daily returns
        """
        prices = price_data["Close"]

        # Handle duplicate indices to prevent reindexing errors
        if prices.index.has_duplicates:
            prices = prices[~prices.index.duplicated(keep="first")]

        returns = prices.pct_change().dropna()
        return returns

    @staticmethod
    def calculate_volatility(
        returns: pd.Series, trading_days: int = TRADING_DAYS_PER_YEAR
    ) -> float:
        """
        Calculate annualized volatility from daily returns

        Args:
            returns: Series of daily returns
            trading_days: Number of trading days in a year

        Returns:
            Annualized volatility as percentage
        """
        daily_std = returns.std()
        annualized_vol = daily_std * np.sqrt(trading_days)
        return annualized_vol * 100

    @staticmethod
    def calculate_stock_metrics(
        ticker: str, name: str, returns: pd.Series
    ) -> StockMetrics:
        """
        Calculate stock metrics from returns

        Args:
            ticker: Stock ticker
            name: Stock name
            returns: Daily returns series

        Returns:
            StockMetrics object
        """
        volatility = MetricsCalculator.calculate_volatility(returns)
        mean_return = returns.mean() * 100
        std_return = returns.std()

        return StockMetrics(
            ticker=ticker,
            name=name,
            volatility_annual=volatility,
            returns_mean=mean_return,
            returns_std=std_return,
        )

    @staticmethod
    def calculate_benchmark_metrics(
        ticker: str, name: str, returns: pd.Series
    ) -> BenchmarkMetrics:
        """
        Calculate benchmark metrics from returns

        Args:
            ticker: Benchmark ticker
            name: Benchmark name
            returns: Daily returns series

        Returns:
            BenchmarkMetrics object
        """
        volatility = MetricsCalculator.calculate_volatility(returns)
        mean_return = returns.mean() * 100

        return BenchmarkMetrics(
            ticker=ticker,
            name=name,
            volatility_annual=volatility,
            returns_mean=mean_return,
        )

    @staticmethod
    def calculate_beta(
        stock_returns: pd.Series, benchmark_returns: pd.Series
    ) -> BetaAnalysisResult:
        """
        Calculate beta of stock relative to benchmark

        Args:
            stock_returns: Series of stock daily returns
            benchmark_returns: Series of benchmark daily returns

        Returns:
            BetaAnalysisResult object
        """
        # Align the data by date
        aligned_data = pd.concat(
            [stock_returns, benchmark_returns], axis=1, join="inner"
        )
        aligned_data.columns = ["Stock", "Benchmark"]

        # Calculate covariance and variance
        covariance = aligned_data["Stock"].cov(aligned_data["Benchmark"])
        benchmark_variance = aligned_data["Benchmark"].var()

        # Calculate beta
        beta = covariance / benchmark_variance if benchmark_variance != 0 else np.nan

        # Calculate correlation and R-squared
        if not np.isnan(beta):
            correlation = aligned_data["Stock"].corr(aligned_data["Benchmark"])
            r_squared = correlation**2
        else:
            correlation = np.nan
            r_squared = np.nan

        return BetaAnalysisResult(
            beta=beta,
            r_squared=r_squared,
            correlation=correlation,
            aligned_data=aligned_data,
        )

    @staticmethod
    def calculate_rolling_volatility(
        returns: pd.Series,
        window_days: int = 30,
        trading_days: int = TRADING_DAYS_PER_YEAR,
    ) -> pd.Series:
        """
        Calculate rolling volatility

        Args:
            returns: Series of daily returns
            window_days: Rolling window in days
            trading_days: Trading days in a year

        Returns:
            Series of rolling annualized volatility
        """
        rolling_std = returns.rolling(window=window_days).std()
        rolling_vol = rolling_std * np.sqrt(trading_days) * 100
        return rolling_vol

    @staticmethod
    def calculate_rolling_beta(
        stock_returns: pd.Series, benchmark_returns: pd.Series, window_days: int = 60
    ) -> pd.DataFrame:
        """
        Calculate rolling beta over time

        Args:
            stock_returns: Series of stock returns
            benchmark_returns: Series of benchmark returns
            window_days: Rolling window in days

        Returns:
            DataFrame with rolling beta and R-squared
        """
        aligned_data = pd.concat(
            [stock_returns, benchmark_returns], axis=1, join="inner"
        )
        aligned_data.columns = ["Stock", "Benchmark"]

        rolling_beta = []
        rolling_corr = []

        for i in range(len(aligned_data)):
            if i < window_days:
                rolling_beta.append(np.nan)
                rolling_corr.append(np.nan)
            else:
                window = aligned_data.iloc[i - window_days : i]
                covariance = window["Stock"].cov(window["Benchmark"])
                benchmark_variance = window["Benchmark"].var()

                if benchmark_variance != 0:
                    beta = covariance / benchmark_variance
                    corr = window["Stock"].corr(window["Benchmark"])
                else:
                    beta = np.nan
                    corr = np.nan

                rolling_beta.append(beta)
                rolling_corr.append(corr)

        result = pd.DataFrame(
            {"Rolling_Beta": rolling_beta, "Rolling_Correlation": rolling_corr},
            index=aligned_data.index,
        )

        result["Rolling_R2"] = result["Rolling_Correlation"] ** 2

        return result[["Rolling_Beta", "Rolling_R2"]]
