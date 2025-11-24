"""
Promotion Forecasting System
=============================
Predicts unit sales for future promotion campaigns based on historical data.
"""

from datetime import datetime

class PromotionForecaster:
    """
    Forecasts promotion sales using item similarity and seasonality.
    
    Features:
    - Item similarity calculation (Jaccard-based)
    - Seasonality boost for same-month promotions
    - Cold start handling for new product categories
    """
    
    def __init__(self):
        print("\n--- Initializing Promotion Forecaster ---")
        self.history = [
            {
                "id": "PROMO_JUNE_2023",
                "items": ["iphone13", "samsung_s22", "macbook_air", "sony_xm4"],
                "units_sold": 5000,
                "date": "2023-06-15"
            },
            {
                "id": "PROMO_JULY_2023",
                "items": ["ps5", "xbox_series_x", "nintendo_switch"],
                "units_sold": 8000,
                "date": "2023-07-10"
            },
            {
                "id": "PROMO_JUNE_2024",
                "items": ["iphone14", "samsung_s23", "macbook_air_m2", "sony_xm5"],
                "units_sold": 5500,
                "date": "2024-06-14"
            },
            {
                "id": "PROMO_DIWALI_2023",
                "items": ["diya", "lights", "sweets_box", "iphone13"],
                "units_sold": 12000,
                "date": "2023-11-10"
            }
        ]

    def calculate_item_similarity(self, historical_items, current_items):
        """
        Calculates item similarity using the formula: |A ∩ B| / |B|
        
        Args:
            historical_items (list): Items from historical promotion
            current_items (list): Items in current promotion
            
        Returns:
            float: Similarity score (coverage)
        """
        set_hist = set(historical_items)
        set_curr = set(current_items)
        intersection = set_hist.intersection(set_curr)
        if len(set_curr) == 0: 
            return 0.0
        return len(intersection) / len(set_curr)

    def get_month_from_date(self, date_str):
        """Extract month from date string."""
        return datetime.strptime(date_str, "%Y-%m-%d").month

    def predict_sales(self, current_promo_items, target_date):
        """
        Predicts sales for a promotion based on historical similarity.
        
        Args:
            current_promo_items (list): Items in the planned promotion
            target_date (str): Target date in YYYY-MM-DD format
            
        Returns:
            tuple: (predicted_units, all_candidates)
        """
        print(f"\nPredicting sales for Promotion on {target_date}")
        print(f"Items: {current_promo_items}")
        
        target_month = self.get_month_from_date(target_date)
        candidates = []
        
        for promo in self.history:
            # Base similarity: Item overlap
            sim_score = self.calculate_item_similarity(promo['items'], current_promo_items)
            
            # Seasonality boost (20% if same month)
            promo_month = self.get_month_from_date(promo['date'])
            seasonality_boost = 0.0
            if promo_month == target_month:
                seasonality_boost = 0.2
                sim_score += seasonality_boost
            
            candidates.append({
                "id": promo['id'],
                "similarity": sim_score,
                "units": promo['units_sold'],
                "items": promo['items'],
                "seasonality_boost": seasonality_boost
            })
        
        # Sort by similarity
        candidates.sort(key=lambda x: x['similarity'], reverse=True)
        top_match = candidates[0]

        # Cold Start handling
        if top_match['similarity'] == 0.0:
            print("   -> Cold Start Detected: No similar historical promotion found.")
            print("   -> Fallback Strategy: Using average of all historical sales.")
            avg_units = sum(p['units_sold'] for p in self.history) / len(self.history)
            return avg_units, candidates

        print(f"\nMost Similar Past Promotion: {top_match['id']}")
        print(f"Similarity Score: {top_match['similarity']:.2f} (includes {top_match['seasonality_boost']} seasonality boost)")
        print(f"Predicted Units: {top_match['units']}")
        
        return top_match['units'], candidates


if __name__ == "__main__":
    # Example usage
    forecaster = PromotionForecaster()
    
    # Test Case: Tech Gadgets Promo
    current_items = ["iphone14", "samsung_s23", "sony_xm5", "new_gadget"]
    predicted_units, details = forecaster.predict_sales(current_items, "2025-06-15")
    
    print(f"\n=== Final Prediction: {predicted_units} units ===")
