"""
Q&A Ranking System
==================
A machine learning system to rank answers for questions on platforms like Quora, Reddit, and Facebook.
"""

import re
import math
from collections import Counter

class QARankingSystem:
    """
    Ranks answers based on text similarity, interaction metrics, and quality filters.
    
    Features:
    - Text preprocessing and Jaccard similarity
    - Interaction metrics (upvotes, CTR, impressions)
    - Spam/quality filtering for short answers
    - Handles negative upvotes safely
    """
    
    def __init__(self):
        print("--- Initializing Q&A Ranking System ---")

    def preprocess_text(self, text):
        """
        Basic text cleaning: lowercase, remove punctuation, tokenize.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            list: List of tokens
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = text.split()
        return tokens

    def calculate_jaccard_similarity(self, query_tokens, doc_tokens):
        """
        Calculates Jaccard similarity between query and document tokens.
        
        Formula: |A ∩ B| / |A ∪ B|
        
        Args:
            query_tokens (list): Tokens from the question
            doc_tokens (list): Tokens from the answer
            
        Returns:
            float: Similarity score between 0 and 1
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
        
        Args:
            question (str): The question text
            answers (list): List of answer dictionaries with 'text', 'upvotes', 'impressions'
            
        Returns:
            list: Sorted list of answers with scores and metrics
        """
        print(f"\nRanking answers for question: '{question}'")
        q_tokens = self.preprocess_text(question)
        
        scored_answers = []
        for ans in answers:
            a_tokens = self.preprocess_text(ans['text'])
            
            # 1. Semantic/Text Match (Jaccard similarity)
            similarity_score = self.calculate_jaccard_similarity(q_tokens, a_tokens)
            
            # 2. Interaction Metrics
            upvotes = ans.get('upvotes', 0)
            impressions = ans.get('impressions', 1)
            ctr = upvotes / impressions if impressions > 0 else 0
            
            # 3. Spam/Quality Penalty
            length_penalty = 0.0
            if len(ans['text'].split()) < 5:
                length_penalty = -0.5
                print(f"   -> Penalty applied to short answer: '{ans['text']}'")

            # Handle negative upvotes safely
            safe_upvotes = max(1, upvotes + 1)
            
            # Final Score: weighted combination
            # Score = 0.6 * Similarity + 2.0 * CTR + 0.1 * log(Upvotes) + Penalty
            final_score = (similarity_score * 0.6) + (ctr * 2.0) + (math.log(safe_upvotes) * 0.1) + length_penalty
            
            scored_answers.append({
                'text': ans['text'],
                'score': final_score,
                'metrics': {
                    'jaccard': similarity_score, 
                    'ctr': ctr, 
                    'upvotes': upvotes, 
                    'penalty': length_penalty
                }
            })
        
        # Sort descending by score
        scored_answers.sort(key=lambda x: x['score'], reverse=True)
        return scored_answers


if __name__ == "__main__":
    # Example usage
    ranker = QARankingSystem()
    
    question = "What is the difference between Batch and Stream processing?"
    answers = [
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
        }
    ]
    
    ranked = ranker.rank_answers(question, answers)
    
    print("\n--- Ranked Results ---")
    for i, r in enumerate(ranked):
        print(f"{i+1}. Score: {r['score']:.2f}")
        print(f"   Text: {r['text'][:80]}...")
        print(f"   Metrics: Jaccard={r['metrics']['jaccard']:.2f}, CTR={r['metrics']['ctr']:.2f}, Upvotes={r['metrics']['upvotes']}")
