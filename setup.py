'''
 # @ Author: Meet Patel
 # @ Create Time: 2026-01-01 12:23:27
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 13:24:09
 # @ Description: Setup script for volatility analysis package
 '''

from setuptools import setup

setup(
    name="volatility_analysis",
    version="0.1.0",
    description="Stock Market Volatility and Beta Analysis Tool",
    packages=["volatility_analysis"],
    package_dir={"volatility_analysis": "."},
    install_requires=[
        "pandas",
        "numpy",
        "yfinance",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "volatility-analysis=volatility_analysis.main:main",
        ],
    },
)