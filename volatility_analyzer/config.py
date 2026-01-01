"""
# @ Author: Meet Patel
# @ Create Time: 2025-12-28 12:54:58
# @ Modified by: Meet Patel
# @ Modified time: 2026-01-01 13:20:42
# @ Description: Configuration and constants for stock volatility analysis
"""

# ============================================================================
# TRADING DAYS CONFIGURATION
# ============================================================================

TRADING_DAYS_PER_YEAR = 252  # Standard US market trading days

# ============================================================================
# DEFAULT ANALYSIS PARAMETERS
# ============================================================================

DEFAULT_YEARS_OF_DATA = 3
DEFAULT_ROLLING_VOLATILITY_WINDOW = 30  # Days
DEFAULT_ROLLING_BETA_WINDOW = 60  # Days

# ============================================================================
# CACHE CONFIGURATION
# ============================================================================

DEFAULT_CACHE_DIR = "yfinance_data"

# ============================================================================
# RISK THRESHOLDS (for categorization)
# ============================================================================

VOLATILITY_THRESHOLDS = {
    "low": 15,  # < 15% annualized volatility
    "moderate": 25,  # 15-25% annualized volatility
    "high": 40,  # 25-40% annualized volatility
    # > 40% = very high
}

BETA_THRESHOLDS = {
    "defensive": 0.8,  # Beta < 0.8
    "neutral": 1.2,  # Beta 0.8-1.2
    "aggressive": 1.5,  # Beta 1.2-1.5
    # Beta > 1.5 = highly aggressive
}
