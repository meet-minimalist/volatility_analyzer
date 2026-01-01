'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 14:28:23
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:22:50
 # @ Description: Visualization utilities for analysis results
 '''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List
from data_models import AnalysisReport


class AnalysisVisualizer:
    """Create visualizations for volatility and beta analysis"""
    
    @staticmethod
    def plot_single_stock_analysis(
        report: AnalysisReport,
        stock_data: pd.DataFrame,
        benchmark_data: pd.DataFrame,
        stock_returns: pd.Series,
        benchmark_returns: pd.Series
    ):
        """
        Create comprehensive visualization for single stock analysis
        
        Args:
            report: AnalysisReport object
            stock_data: Stock price data
            benchmark_data: Benchmark price data
            stock_returns: Stock returns
            benchmark_returns: Benchmark returns
        """
        fig, axes = plt.subplots(3, 2, figsize=(15, 12))
        fig.suptitle(
            f'Volatility & Beta Analysis: {report.stock_metrics.name} vs {report.benchmark_metrics.name}',
            fontsize=16, fontweight='bold'
        )
        
        # Plot 1: Normalized price performance
        AnalysisVisualizer._plot_price_comparison(
            axes[0, 0], stock_data, benchmark_data,
            report.stock_metrics.name, report.benchmark_metrics.name
        )
        
        # Plot 2: Returns distribution
        AnalysisVisualizer._plot_returns_distribution(
            axes[0, 1], stock_returns, benchmark_returns,
            report.stock_metrics.name, report.benchmark_metrics.name
        )
        
        # Plot 3: Rolling volatility
        AnalysisVisualizer._plot_rolling_volatility(
            axes[1, 0], report.rolling_volatility
        )
        
        # Plot 4: Rolling beta
        AnalysisVisualizer._plot_rolling_beta(
            axes[1, 1], report.rolling_metrics
        )
        
        # Plot 5: Scatter plot with regression
        AnalysisVisualizer._plot_scatter_regression(
            axes[2, 0], report.beta_analysis.aligned_data,
            report.stock_metrics.name, report.benchmark_metrics.name,
            report.beta_analysis.beta, report.beta_analysis.r_squared
        )
        
        # Plot 6: R-squared over time
        AnalysisVisualizer._plot_r_squared(
            axes[2, 1], report.rolling_metrics
        )
        
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def _plot_price_comparison(ax, stock_data, benchmark_data, stock_name, benchmark_name):
        """Plot normalized price comparison"""
        norm_stock = stock_data['Close'] / stock_data['Close'].iloc[0]
        norm_bench = benchmark_data['Close'] / benchmark_data['Close'].iloc[0]
        ax.plot(norm_stock.index, norm_stock, label=stock_name, linewidth=2)
        ax.plot(norm_bench.index, norm_bench, label=benchmark_name, linewidth=2, alpha=0.7)
        ax.set_title('Normalized Price Performance')
        ax.set_ylabel('Normalized Price (Base=100)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def _plot_returns_distribution(ax, stock_returns, benchmark_returns, stock_name, benchmark_name):
        """Plot returns distribution histogram"""
        ax.hist(stock_returns, bins=50, alpha=0.7, label=stock_name, density=True)
        ax.hist(benchmark_returns, bins=50, alpha=0.7, label=benchmark_name, density=True)
        ax.axvline(x=0, color='black', linestyle='--', alpha=0.5)
        ax.set_title('Distribution of Daily Returns')
        ax.set_xlabel('Daily Return')
        ax.set_ylabel('Density')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def _plot_rolling_volatility(ax, rolling_vol):
        """Plot rolling volatility over time"""
        ax.plot(rolling_vol.index, rolling_vol, color='red', linewidth=1.5)
        mean_vol = rolling_vol.mean()
        ax.axhline(y=mean_vol, color='black', linestyle='--', label=f'Mean: {mean_vol:.1f}%')
        ax.fill_between(rolling_vol.index, rolling_vol, mean_vol,
                        where=(rolling_vol > mean_vol),
                        color='red', alpha=0.2, label='Above Average')
        ax.fill_between(rolling_vol.index, rolling_vol, mean_vol,
                        where=(rolling_vol <= mean_vol),
                        color='green', alpha=0.2, label='Below Average')
        ax.set_title('30-Day Rolling Annualized Volatility')
        ax.set_ylabel('Volatility (%)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def _plot_rolling_beta(ax, rolling_metrics):
        """Plot rolling beta over time"""
        ax.plot(rolling_metrics.index, rolling_metrics['Rolling_Beta'],
                color='blue', linewidth=1.5)
        ax.axhline(y=1.0, color='black', linestyle='--', label='Beta = 1 (Market)')
        ax.fill_between(rolling_metrics.index, rolling_metrics['Rolling_Beta'], 1.0,
                        where=(rolling_metrics['Rolling_Beta'] > 1.0),
                        color='red', alpha=0.2, label='Beta > 1')
        ax.fill_between(rolling_metrics.index, rolling_metrics['Rolling_Beta'], 1.0,
                        where=(rolling_metrics['Rolling_Beta'] <= 1.0),
                        color='green', alpha=0.2, label='Beta ≤ 1')
        ax.set_title('60-Day Rolling Beta')
        ax.set_ylabel('Beta')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def _plot_scatter_regression(ax, aligned_data, stock_name, benchmark_name, beta, r_squared):
        """Plot scatter plot with regression line"""
        ax.scatter(aligned_data['Benchmark']*100, aligned_data['Stock']*100,
                   alpha=0.5, s=10)
        
        # Add regression line
        z = np.polyfit(aligned_data['Benchmark']*100, aligned_data['Stock']*100, 1)
        p = np.poly1d(z)
        ax.plot(aligned_data['Benchmark']*100, p(aligned_data['Benchmark']*100),
                "r--", alpha=0.8, label=f'Beta = {z[0]:.2f}')
        
        ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax.set_xlabel(f'{benchmark_name} Daily Return (%)')
        ax.set_ylabel(f'{stock_name} Daily Return (%)')
        ax.set_title(f'Scatter: Stock vs Benchmark Returns\nBeta = {beta:.2f}, R² = {r_squared:.2f}')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def _plot_r_squared(ax, rolling_metrics):
        """Plot R-squared over time"""
        ax.plot(rolling_metrics.index, rolling_metrics['Rolling_R2'],
                color='purple', linewidth=1.5)
        ax.fill_between(rolling_metrics.index, rolling_metrics['Rolling_R2'],
                        alpha=0.3, color='purple')
        ax.set_title('60-Day Rolling R-squared')
        ax.set_ylabel('R-squared')
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)
    
    @staticmethod
    def plot_comparison(comparison_df: pd.DataFrame):
        """
        Plot comparison of multiple stocks
        
        Args:
            comparison_df: DataFrame with comparison data
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        stocks = comparison_df['Ticker'].str.replace('.NS', '').str.replace('.BO', '')
        
        # Plot 1: Volatility comparison
        AnalysisVisualizer._plot_volatility_comparison(axes[0, 0], stocks, comparison_df)
        
        # Plot 2: Beta comparison
        AnalysisVisualizer._plot_beta_comparison(axes[0, 1], stocks, comparison_df)
        
        # Plot 3: Volatility ratio
        AnalysisVisualizer._plot_volatility_ratio(axes[1, 0], stocks, comparison_df)
        
        # Plot 4: R-squared comparison
        AnalysisVisualizer._plot_r_squared_comparison(axes[1, 1], stocks, comparison_df)
        
        plt.suptitle('Multi-Stock Volatility & Beta Comparison',
                     fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def _plot_volatility_comparison(ax, stocks, df):
        """Plot volatility comparison bars"""
        volatilities = df['Volatility_Pct']
        median = volatilities.median()
        colors = ['red' if v > median else 'green' for v in volatilities]
        bars = ax.barh(stocks, volatilities, color=colors)
        ax.set_xlabel('Annualized Volatility (%)')
        ax.set_title('Volatility Comparison')
        ax.axvline(x=median, color='blue', linestyle='--',
                   label=f'Median: {median:.1f}%')
        ax.legend()
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                    f'{width:.1f}%', va='center')
    
    @staticmethod
    def _plot_beta_comparison(ax, stocks, df):
        """Plot beta comparison bars"""
        betas = df['Beta']
        colors = ['red' if b > 1.2 else 'orange' if b > 0.8 else 'green' for b in betas]
        bars = ax.barh(stocks, betas, color=colors)
        ax.set_xlabel('Beta')
        ax.set_title('Beta Comparison')
        ax.axvline(x=1.0, color='black', linestyle='--', label='Beta = 1 (Market)')
        ax.legend()
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.02, bar.get_y() + bar.get_height()/2,
                    f'{width:.2f}', va='center')
    
    @staticmethod
    def _plot_volatility_ratio(ax, stocks, df):
        """Plot volatility ratio bars"""
        ratios = df['Volatility_Ratio']
        colors = ['red' if r > 1.5 else 'orange' if r > 1.0 else 'green' for r in ratios]
        bars = ax.barh(stocks, ratios, color=colors)
        ax.set_xlabel('Volatility Ratio (Stock/Benchmark)')
        ax.set_title('Relative Volatility (vs Benchmark)')
        ax.axvline(x=1.0, color='black', linestyle='--',
                   label='Same as Benchmark')
        ax.legend()
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.02, bar.get_y() + bar.get_height()/2,
                    f'{width:.2f}x', va='center')
    
    @staticmethod
    def _plot_r_squared_comparison(ax, stocks, df):
        """Plot R-squared comparison bars"""
        r2_values = df['R_Squared'] * 100
        colors = ['green' if r > 50 else 'orange' if r > 25 else 'red' for r in r2_values]
        bars = ax.barh(stocks, r2_values, color=colors)
        ax.set_xlabel('R-squared (%)')
        ax.set_title('Goodness of Fit (R-squared)')
        ax.set_xlim(0, 100)
        ax.axvline(x=50, color='blue', linestyle='--',
                   label='50% explained by market')
        ax.legend()
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2,
                    f'{width:.1f}%', va='center')
