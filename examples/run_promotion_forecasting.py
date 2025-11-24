"""
Promotion Forecasting - Example Usage
======================================
Demonstrates how to use the promotion forecasting system.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from promotion_forecasting.promo_forecaster import PromotionForecaster

def example_tech_promo():
    """Example: Tech gadgets promotion."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Tech Gadgets Promotion")
    print("="*60)
    
    forecaster = PromotionForecaster()
    current_items = ["iphone14", "samsung_s23", "sony_xm5", "new_gadget"]
    predicted_units, candidates = forecaster.predict_sales(current_items, "2025-06-15")
    
    print(f"\n=== Prediction: {predicted_units} units ===")


def example_seasonal_promo():
    """Example: Winter promotion with seasonality boost."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Winter Promotion (Seasonality)")
    print("="*60)
    
    forecaster = PromotionForecaster()
    
    # Add winter promotion to history
    forecaster.history.append({
        "id": "PROMO_WINTER_SALE_2023",
        "items": ["heater", "blanket", "jacket", "gloves"],
        "units_sold": 3000,
        "date": "2023-12-01"
    })
    
    current_items = ["heater", "wool_socks", "jacket", "thermals"]
    predicted_units, candidates = forecaster.predict_sales(current_items, "2025-12-10")
    
    print(f"\n=== Prediction: {predicted_units} units ===")


def example_cold_start():
    """Example: New category with no historical data."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Cold Start (New Category)")
    print("="*60)
    
    forecaster = PromotionForecaster()
    current_items = ["gardening_tools", "seeds", "fertilizer"]
    predicted_units, candidates = forecaster.predict_sales(current_items, "2025-03-01")
    
    print(f"\n=== Prediction: {predicted_units:.0f} units (Average Fallback) ===")


if __name__ == "__main__":
    example_tech_promo()
    example_seasonal_promo()
    example_cold_start()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
