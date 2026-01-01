'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 14:26:49
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:21:47
 # @ Description: Data models for volatility analysis results
 '''


from dataclasses import dataclass
from typing import Optional
import pandas as pd

from volatility_analyzer.logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class StockMetrics:
    """Encapsulates volatility and return metrics for a stock"""
    ticker: str
    name: str
    volatility_annual: float  # Percentage
    returns_mean: float  # Daily mean as percentage
    returns_std: float  # Daily standard deviation
    
    def __str__(self):
        return (f"{self.name} ({self.ticker}): "
                f"Vol={self.volatility_annual:.2f}%, "
                f"Mean Return={self.returns_mean:.4f}%")


@dataclass
class BenchmarkMetrics:
    """Encapsulates benchmark metrics"""
    ticker: str
    name: str
    volatility_annual: float
    returns_mean: float
    
    def __str__(self):
        return (f"{self.name} ({self.ticker}): "
                f"Vol={self.volatility_annual:.2f}%")


@dataclass
class BetaAnalysisResult:
    """Results of beta analysis"""
    beta: float
    r_squared: float
    correlation: float
    aligned_data: pd.DataFrame
    
    def interpretation(self) -> str:
        """Get human-readable interpretation of beta"""
        if self.beta > 1.5:
            return "Highly volatile stock, amplifies market movements"
        elif self.beta > 1.0:
            return "More volatile than market"
        elif self.beta == 1.0:
            return "Moves in line with market"
        elif self.beta > 0:
            return "Less volatile than market"
        else:
            return "Moves inversely to market (defensive)"


@dataclass
class AnalysisReport:
    """Complete analysis report for a stock"""
    stock_metrics: StockMetrics
    benchmark_metrics: BenchmarkMetrics
    beta_analysis: BetaAnalysisResult
    period_start: str
    period_end: str
    data_points: int
    volatility_ratio: float
    rolling_volatility: pd.Series
    rolling_metrics: pd.DataFrame
    
    def to_dict(self) -> dict:
        """Convert to dictionary format"""
        return {
            'Stock': self.stock_metrics.name,
            'Ticker': self.stock_metrics.ticker,
            'Benchmark': self.benchmark_metrics.name,
            'Benchmark_Ticker': self.benchmark_metrics.ticker,
            'Period': f"{self.period_start} to {self.period_end}",
            'Stock_Volatility_Annual': f"{self.stock_metrics.volatility_annual:.2f}%",
            'Benchmark_Volatility_Annual': f"{self.benchmark_metrics.volatility_annual:.2f}%",
            'Beta': round(self.beta_analysis.beta, 3),
            'R_Squared': round(self.beta_analysis.r_squared, 3),
            'Volatility_Ratio': round(self.volatility_ratio, 2),
            'Data_Points': self.data_points,
            'Stock_Returns_Mean': f"{self.stock_metrics.returns_mean:.4f}%",
            'Benchmark_Returns_Mean': f"{self.benchmark_metrics.returns_mean:.4f}%",
        }
    
    def log_report(self):
        """Log formatted analysis report"""
        report_lines = [
            "="*60,
            "VOLATILITY & BETA ANALYSIS REPORT",
            "="*60,
            f"Stock: {self.stock_metrics.name} ({self.stock_metrics.ticker})",
            f"Benchmark: {self.benchmark_metrics.name}",
            f"Analysis Period: {self.period_start} to {self.period_end}",
            f"Data Points: {self.data_points} trading days",
            "\n--- VOLATILITY ANALYSIS ---",
            f"Stock Annualized Volatility: {self.stock_metrics.volatility_annual:.2f}%",
            f"Benchmark Annualized Volatility: {self.benchmark_metrics.volatility_annual:.2f}%",
            f"Volatility Ratio (Stock/Benchmark): {self.volatility_ratio:.2f}x",
            "\n--- BETA ANALYSIS ---",
            f"Beta: {self.beta_analysis.beta:.3f}",
            f"R-squared: {self.beta_analysis.r_squared:.3f} "
            f"({self.beta_analysis.r_squared*100:.1f}% of moves explained by benchmark)",
            "\nBeta Interpretation:",
            f"  → {self.beta_analysis.interpretation()}",
            "\n--- RETURNS ---",
            f"Stock Avg Daily Return: {self.stock_metrics.returns_mean:.4f}%",
            f"Benchmark Avg Daily Return: {self.benchmark_metrics.returns_mean:.4f}%",
            "="*60
        ]
        logger.info("\n".join(report_lines))
