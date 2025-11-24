"""
Q&A Ranking System - Example Usage
===================================
Demonstrates how to use the Q&A ranking system with various scenarios.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qa_ranking.qa_ranker import QARankingSystem

def example_technical_question():
    """Example: Technical question about data processing."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Technical Question")
    print("="*60)
    
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
        },
        {
            "text": "Check out this link for a tutorial.", 
            "upvotes": 10, 
            "impressions": 50
        }
    ]
    
    ranked = ranker.rank_answers(question, answers)
    
    print(f"\nQuestion: '{question}'")
    print("\nRanked Answers:")
    for i, r in enumerate(ranked):
        print(f"\n{i+1}. Score: {r['score']:.2f}")
        print(f"   Text: {r['text'][:70]}...")
        print(f"   Metrics: Jaccard={r['metrics']['jaccard']:.3f}, CTR={r['metrics']['ctr']:.3f}, Upvotes={r['metrics']['upvotes']}")


def example_opinion_question():
    """Example: Opinion-based question."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Opinion Question")
    print("="*60)
    
    ranker = QARankingSystem()
    
    question = "Is Python better than Java for Machine Learning?"
    answers = [
        {
            "text": "Yes, Python has better libraries like PyTorch and TensorFlow for ML tasks.", 
            "upvotes": 500, 
            "impressions": 2000
        },
        {
            "text": "Java is faster but Python is easier to write and has more ML support.", 
            "upvotes": 200, 
            "impressions": 800
        },
        {
            "text": "C++ is the best.", 
            "upvotes": -5, 
            "impressions": 300
        }
    ]
    
    ranked = ranker.rank_answers(question, answers)
    
    print(f"\nQuestion: '{question}'")
    print("\nRanked Answers:")
    for i, r in enumerate(ranked):
        print(f"\n{i+1}. Score: {r['score']:.2f}")
        print(f"   Text: {r['text']}")
        print(f"   Upvotes: {r['metrics']['upvotes']}, Penalty: {r['metrics']['penalty']}")


def example_spam_detection():
    """Example: Demonstrating spam filtering."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Spam Detection")
    print("="*60)
    
    ranker = QARankingSystem()
    
    question = "How to learn system design?"
    answers = [
        {
            "text": "Read 'Designing Data-Intensive Applications' by Martin Kleppmann and practice with real-world case studies.", 
            "upvotes": 300, 
            "impressions": 1000
        },
        {
            "text": "Yes.", 
            "upvotes": 2, 
            "impressions": 50
        },
        {
            "text": "Watch YouTube tutorials and take online courses on platforms like Coursera or Udemy.", 
            "upvotes": 150, 
            "impressions": 600
        }
    ]
    
    ranked = ranker.rank_answers(question, answers)
    
    print(f"\nQuestion: '{question}'")
    print("\nRanked Answers (Note: Short answers get penalized):")
    for i, r in enumerate(ranked):
        print(f"\n{i+1}. Score: {r['score']:.2f}")
        print(f"   Text: {r['text']}")
        print(f"   Penalty: {r['metrics']['penalty']}")


if __name__ == "__main__":
    example_technical_question()
    example_opinion_question()
    example_spam_detection()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
