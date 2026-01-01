# Volatility Analysis

A Python package for analyzing stock market volatility and beta.

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/meet-minimalist/yf_cache.git
```

Or from source:
```bash
pip install .
```

## Usage

```python
from volatility_analyzer import VolatilityAnalyzer

report, stock_data, benchmark_data = analyzer.analyze_stock(
    "RELIANCE.NS",
    plot_results=True
)
```