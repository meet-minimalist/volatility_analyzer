'''
 # @ Author: Meet Patel
 # @ Create Time: 2026-01-01 14:18:28
 # @ Modified by: Meet Patel
 # @ Modified time: 2026-01-01 14:19:18
 # @ Description:
 '''

'''
Example 2: Specific Metrics Request
'''

import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from volatility_analyzer import VolatilityAnalyzer

def run_example():
    logging.basicConfig(level=logging.INFO)
    analyzer = VolatilityAnalyzer(years_of_data=3)
    
    print("\n\n" + "="*80)
    print("EXAMPLE 1.5: Specific Metrics Request")
    print("="*80)
    
    # Note: The 'analyze' method with 'methods' parameter might need to be implemented 
    # in VolatilityAnalyzer if it doesn't exist yet.
    try:
        results = analyzer.analyze("NVDA", methods=['stddev', 'beta'])
        print(f"Analysis Results for NVDA: {results}")
    except AttributeError:
        print("Feature not implemented: 'analyze' method missing in VolatilityAnalyzer")

if __name__ == "__main__":
    run_example()