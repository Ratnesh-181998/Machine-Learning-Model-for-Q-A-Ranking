import re
import math
from collections import Counter
from datetime import datetime

# ==========================================
# PART 1: Q&A Ranking System (Quora/Reddit)
# ==========================================

class QARankingSystem:
    def __init__(self):
        print("--- Initializing Q&A Ranking System ---")

    def preprocess_text(self, text):
        """
        Basic text cleaning: lowercase, remove punctuation, tokenize.
        Corresponds to 'Text Processing' in notes.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = text.split()
        return tokens

    def calculate_jaccard_similarity(self, query_tokens, doc_tokens):
        """
        Calculates Jaccard similarity between query and document tokens.
        """
        set_query = set(query_tokens)
        set_doc = set(doc_tokens)
        
        intersection = len(set_query.intersection(set_doc))
        union = len(set_query.union(set_doc))
        
        return intersection / union if union > 0 else 0.0

    def rank_answers(self, question, answers):
        """
        Ranks answers based on a hybrid score of text similarity and interaction metrics.
        Includes a basic Spam/Quality filter.
        """
        print(f"Ranking answers for question: '{question}'")
        q_tokens = self.preprocess_text(question)
        
        scored_answers = []
        for ans in answers:
            a_tokens = self.preprocess_text(ans['text'])
            
            # 1. Semantic/Text Match (Mocked by Jaccard)
            similarity_score = self.calculate_jaccard_similarity(q_tokens, a_tokens)
            
            # 2. Interaction Metrics
            upvotes = ans.get('upvotes', 0)
            impressions = ans.get('impressions', 1)
            ctr = upvotes / impressions if impressions > 0 else 0
            
            # 3. Spam/Quality Penalty (Edge Case)
            # Penalize very short answers (e.g., "I don't know", "Yes")
            length_penalty = 0.0
            if len(ans['text'].split()) < 5:
                length_penalty = -0.5
                print(f"   -> Penalty applied to short answer: '{ans['text']}'")

            # Handle negative upvotes safely for log calculation
            safe_upvotes = max(1, upvotes + 1)
            
            # Final Score Calculation
            final_score = (similarity_score * 0.6) + (ctr * 2.0) + (math.log(safe_upvotes) * 0.1) + length_penalty
            
            scored_answers.append({
                'text': ans['text'],
                'score': final_score,
                'metrics': {'jaccard': similarity_score, 'ctr': ctr, 'upvotes': upvotes, 'penalty': length_penalty}
            })
        
        # Sort descending
        scored_answers.sort(key=lambda x: x['score'], reverse=True)
        return scored_answers


# ==========================================
# PART 2: Promotion Forecasting (Amazon/Flipkart)
# ==========================================

class PromotionForecaster:
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
        set_hist = set(historical_items)
        set_curr = set(current_items)
        intersection = set_hist.intersection(set_curr)
        if len(set_curr) == 0: return 0.0
        return len(intersection) / len(set_curr)

    def get_month_from_date(self, date_str):
        return datetime.strptime(date_str, "%Y-%m-%d").month

    def predict_sales(self, current_promo_items, target_date):
        print(f"Predicting sales for Promotion on {target_date} with items: {current_promo_items}")
        
        target_month = self.get_month_from_date(target_date)
        candidates = []
        
        for promo in self.history:
            # Base Similarity: Item Overlap
            sim_score = self.calculate_item_similarity(promo['items'], current_promo_items)
            
            # Feature: Seasonality Boost
            # If the historical promo was in the same month, boost score by 20%
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

        # Edge Case: Cold Start (No similar promotion found)
        if top_match['similarity'] == 0.0:
            print("   -> Cold Start Detected: No similar historical promotion found.")
            print("   -> Fallback Strategy: Using average of all historical sales.")
            avg_units = sum(p['units_sold'] for p in self.history) / len(self.history)
            return avg_units, candidates

        print(f"Most Similar Past Promotion: {top_match['id']} (Score: {top_match['similarity']:.2f} [Incl. {top_match['seasonality_boost']} Seasonality])")
        print(f"Predicted Units: {top_match['units']}")
        
        return top_match['units'], candidates

def main():
    # ==========================================
    # DEMO 1: Q&A Ranking System
    # ==========================================
    print("\n" + "="*40)
    print(" DEMO 1: Q&A Ranking System")
    print("="*40)
    qa_system = QARankingSystem()
    
    # Scenario A: Technical Question
    question_1 = "What is the difference between Batch and Stream processing?"
    answers_1 = [
        {
            "text": "Batch processing deals with static data in large chunks, while stream processing deals with continuous data in real-time.", 
            "upvotes": 350, 
            "impressions": 1200
        },
        {
            "text": "I think batch is faster.", 
            "upvotes": 5, 
            "impressions": 100
        },
        {
            "text": "Stream processing is like a river, batch is like a bucket. Apache Flink is good for streaming.", 
            "upvotes": 120, 
            "impressions": 500
        },
        {
            "text": "Check out this link for a tutorial.", 
            "upvotes": 10, 
            "impressions": 50
        }
    ]
    
    ranked_1 = qa_system.rank_answers(question_1, answers_1)
    print(f"\nQuestion: '{question_1}'")
    for i, r in enumerate(ranked_1):
        print(f"{i+1}. Score: {r['score']:.2f} | Text: {r['text'][:60]}...")

    # Scenario B: Opinion Question
    question_2 = "Is Python better than Java for ML?"
    answers_2 = [
        {"text": "Yes, Python has better libraries like PyTorch and TensorFlow.", "upvotes": 500, "impressions": 2000},
        {"text": "Java is faster but Python is easier to write.", "upvotes": 200, "impressions": 800},
        {"text": "C++ is the best.", "upvotes": -5, "impressions": 300} # Negative upvotes scenario
    ]
    
    ranked_2 = qa_system.rank_answers(question_2, answers_2)
    print(f"\nQuestion: '{question_2}'")
    for i, r in enumerate(ranked_2):
        print(f"{i+1}. Score: {r['score']:.2f} | Text: {r['text']}")


    # ==========================================
    # DEMO 2: Promotion Forecasting
    # ==========================================
    print("\n" + "="*40)
    print(" DEMO 2: Promotion Forecasting")
    print("="*40)
    forecaster = PromotionForecaster()
    
    # Add more historical data for the demo
    forecaster.history.extend([
        {
            "id": "PROMO_WINTER_SALE_2023",
            "items": ["heater", "blanket", "jacket", "gloves"],
            "units_sold": 3000,
            "date": "2023-12-01"
        },
        {
            "id": "PROMO_SUMMER_SPLASH_2023",
            "items": ["ac", "fan", "cooler", "sunglasses", "swimwear"],
            "units_sold": 4500,
            "date": "2023-05-20"
        }
    ])

    # Test Case 1: Tech Gadgets Promo (Matches June 2024)
    current_items_1 = ["iphone14", "samsung_s23", "sony_xm5", "new_gadget"] 
    print(f"\n--- Test Case 1: Tech Promo ---")
    forecaster.predict_sales(current_items_1, "2025-06-15")

    # Test Case 2: Winter Essentials Promo (Matches Winter Sale 2023)
    current_items_2 = ["heater", "wool_socks", "jacket", "thermals"]
    print(f"\n--- Test Case 2: Winter Promo ---")
    forecaster.predict_sales(current_items_2, "2025-12-10")

    # Test Case 3: Mixed/New Promo (Low similarity expected)
    current_items_3 = ["gardening_tools", "seeds", "fertilizer"]
    print(f"\n--- Test Case 3: Gardening Promo (New Category) ---")
    forecaster.predict_sales(current_items_3, "2025-03-01")

if __name__ == "__main__":
    main()
