'''
 # @ Author: Meet Patel
 # @ Create Time: 2025-12-28 12:54:58
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:20:42
 # @ Description: Configuration and constants for stock volatility analysis
 '''

# ============================================================================
# STOCK TO BENCHMARK MAPPING
# ============================================================================

STOCK_BENCHMARK_MAP = {
    # ========== RARE EARTH & MINING ETFs/STOCKS ==========
    'REMX': '^GSPC',      # VanEck Rare Earth/Strategic Metals ETF -> S&P 500
    'MP': '^GSPC',        # MP Materials (Rare Earth) -> S&P 500
    'UUUU': '^GSPC',      # Energy Fuels (Uranium/Rare Earth) -> S&P 500
    
    # ========== MINING & METALS ==========
    'NB': '^GSPC',        # NioCorp (Niobium/Rare Earth) -> S&P 500
    'TGB': '^GSPC',       # Taseko Mines (Copper) -> S&P 500
    
    # ========== SILVER & PRECIOUS METALS ETF/STOCKS ==========
    'SILJ': 'GLD',        # ETFMG Prime Junior Silver ETF -> Gold ETF as proxy
    'AG': 'SLV',          # First Majestic Silver -> Silver ETF
    'CDE': 'SLV',         # Coeur Mining (Silver/Gold) -> Silver ETF
    'HL': 'SLV',          # Hecla Mining (Silver/Gold) -> Silver ETF
    'PAAS': 'SLV',        # Pan American Silver -> Silver ETF
    'WPM': 'GLD',         # Wheaton Precious Metals -> Gold ETF
    'SLV': '^GSPC',       # iShares Silver Trust -> S&P 500
    'ASM': 'SLV',         # Avino Silver & Gold -> Silver ETF
    
    # ========== TECH ETFs ==========
    'QQQ': '^GSPC',       # Nasdaq-100 ETF -> S&P 500 (for relative performance)
    'SMH': 'QQQ',         # VanEck Semiconductor ETF -> Nasdaq-100
    
    # ========== MEGA-CAP TECH STOCKS ==========
    'AMD': 'SMH',         # AMD -> Semiconductor ETF
    'NVDA': 'SMH',        # NVIDIA -> Semiconductor ETF
    'QCOM': 'SMH',        # Qualcomm -> Semiconductor ETF
    'GOOG': 'QQQ',        # Alphabet -> Nasdaq-100
    
    # ========== INDIAN STOCKS (for reference) ==========
    'RELIANCE.NS': '^NSEI',
    'TCS.NS': '^NSEI',
    'HDFCBANK.NS': '^NSEI',
    'INFY.NS': '^NSEI',
    'HINDUNILVR.NS': '^NSEI',
    'ICICIBANK.NS': '^NSEI',
    'KOTAKBANK.NS': '^NSEI',
    'SBIN.NS': '^NSEI',
    'BHARTIARTL.NS': '^NSEI',
    'ITC.NS': '^NSEI',
}

# ============================================================================
# BENCHMARK ALTERNATIVES (FALLBACK)
# ============================================================================

BENCHMARK_ALTERNATIVES = {
    '^GSPC': '^DJI',      # If S&P 500 fails, use Dow Jones
    '^NSEI': '^NSEBANK',  # If Nifty 50 fails, try Nifty Bank
    '^BSESN': '^NSEI',    # If Sensex fails, try Nifty 50
    'QQQ': '^GSPC',       # If QQQ fails, use S&P 500
    'SMH': 'QQQ',         # If SMH fails, use QQQ
    'SLV': 'GLD',         # If Silver fails, use Gold
    'GLD': '^GSPC',       # If Gold fails, use S&P 500
}

# ============================================================================
# STOCK CATEGORIES (for grouping and analysis)
# ============================================================================

STOCK_CATEGORIES = {
    'rare_earth_mining': ['REMX', 'MP', 'UUUU', 'NB', 'TGB'],
    'silver_precious_metals': ['SILJ', 'AG', 'CDE', 'HL', 'PAAS', 'WPM', 'SLV', 'ASM'],
    'tech_etfs': ['QQQ', 'SMH'],
    'semiconductors': ['AMD', 'NVDA', 'QCOM'],
    'mega_cap_tech': ['GOOG', 'NVDA', 'AMD'],
    'all_tech': ['QQQ', 'SMH', 'AMD', 'GOOG', 'NVDA', 'QCOM'],
    'all_materials': ['REMX', 'NB', 'UUUU', 'MP', 'TGB', 'SILJ', 'AG', 'CDE', 'HL', 'PAAS', 'WPM', 'SLV', 'ASM'],
}

# Full portfolio list
ALL_TRACKED_STOCKS = [
    'REMX', 'NB', 'UUUU', 'MP', 'TGB',           # Rare Earth & Mining
    'SILJ', 'AG', 'CDE', 'HL', 'PAAS', 'WPM', 'SLV', 'ASM',  # Silver & Precious Metals
    'QQQ', 'SMH',                                 # Tech ETFs
    'AMD', 'GOOG', 'NVDA', 'QCOM',               # Tech Stocks
]

# ============================================================================
# TRADING DAYS CONFIGURATION
# ============================================================================

TRADING_DAYS_PER_YEAR = 252  # Standard US market trading days

# ============================================================================
# DEFAULT ANALYSIS PARAMETERS
# ============================================================================

DEFAULT_YEARS_OF_DATA = 3
DEFAULT_ROLLING_VOLATILITY_WINDOW = 30  # Days
DEFAULT_ROLLING_BETA_WINDOW = 60        # Days

# ============================================================================
# CACHE CONFIGURATION
# ============================================================================

DEFAULT_CACHE_DIR = "yfinance_data"

# ============================================================================
# STOCK DESCRIPTIONS (Optional - for reporting)
# ============================================================================

STOCK_DESCRIPTIONS = {
    # Rare Earth & Mining
    'REMX': 'VanEck Rare Earth/Strategic Metals ETF',
    'MP': 'MP Materials - Rare Earth Mining',
    'UUUU': 'Energy Fuels - Uranium & Rare Earth',
    'NB': 'NioCorp - Niobium & Rare Earth',
    'TGB': 'Taseko Mines - Copper Mining',
    
    # Silver & Precious Metals
    'SILJ': 'ETFMG Prime Junior Silver Miners ETF',
    'AG': 'First Majestic Silver Corp',
    'CDE': 'Coeur Mining - Silver & Gold',
    'HL': 'Hecla Mining - Silver & Gold',
    'PAAS': 'Pan American Silver Corp',
    'WPM': 'Wheaton Precious Metals',
    'SLV': 'iShares Silver Trust ETF',
    'ASM': 'Avino Silver & Gold Mines',
    
    # Tech ETFs
    'QQQ': 'Invesco QQQ - Nasdaq-100 ETF',
    'SMH': 'VanEck Semiconductor ETF',
    
    # Tech Stocks
    'AMD': 'Advanced Micro Devices',
    'GOOG': 'Alphabet Inc (Google)',
    'NVDA': 'NVIDIA Corporation',
    'QCOM': 'Qualcomm Inc',
}

# ============================================================================
# RISK THRESHOLDS (for categorization)
# ============================================================================

VOLATILITY_THRESHOLDS = {
    'low': 15,        # < 15% annualized volatility
    'moderate': 25,   # 15-25% annualized volatility
    'high': 40,       # 25-40% annualized volatility
    # > 40% = very high
}

BETA_THRESHOLDS = {
    'defensive': 0.8,      # Beta < 0.8
    'neutral': 1.2,        # Beta 0.8-1.2
    'aggressive': 1.5,     # Beta 1.2-1.5
    # Beta > 1.5 = highly aggressive
}

# ============================================================================
# SECTOR BENCHMARKS (Alternative benchmarks by sector)
# ============================================================================

SECTOR_BENCHMARKS = {
    'materials': 'XLB',        # Materials Select Sector SPDR
    'technology': 'XLK',       # Technology Select Sector SPDR
    'semiconductors': 'SMH',   # VanEck Semiconductor ETF
    'precious_metals': 'GLD',  # Gold ETF
    'silver': 'SLV',          # Silver ETF
}

# ============================================================================
# CORRELATION GROUPS (Expected correlation patterns)
# ============================================================================

EXPECTED_HIGH_CORRELATION = [
    ('AMD', 'NVDA'),      # Both semiconductor stocks
    ('AG', 'CDE'),        # Both silver miners
    ('QQQ', 'SMH'),       # Tech ETFs
    ('PAAS', 'HL'),       # Silver miners
]

EXPECTED_LOW_CORRELATION = [
    ('GOOG', 'AG'),       # Tech vs Silver
    ('QQQ', 'SILJ'),      # Tech vs Metals
    ('NVDA', 'WPM'),      # Semiconductors vs Precious Metals
]