# Machine Learning Model for Q&A Ranking

## Overview
This repository contains a comprehensive implementation of a Machine Learning system for ranking answers in Q&A platforms like Quora, Reddit, and Facebook Communities, along with an E-commerce Promotion Forecasting system.

## Contents
- `notes.md`: Comprehensive revision notes covering problem statement, system design components, feature engineering, and modeling strategy.
- `QARankingSystem_PromotionForecaster.py`: Python script implementing both the Q&A Ranking logic and the Promotion Forecasting logic.

## Key Topics
- **Feature Engineering**: Jaccard similarity, text processing, semantic embeddings.
- **Modeling**: Baseline supervised models vs. Advanced LLMs/Ranking models (TensorFlow Ranking).
- **Metrics**: NDCG, MRR, Precision, Recall.

## Case Studies

### 1. Q&A Ranking System
Design a Machine Learning system to rank answers based on relevance, ensuring users see the best possible responses first.

**Key Features:**
- Text processing and semantic embeddings (Sentence-BERT)
- Interaction metrics (upvotes, CTR, dwell time)
- Spam filtering for low-quality answers
- Scalability to millions of Q&A pairs with <100ms latency

### 2. E-commerce Promotion Forecasting
Predict unit sales for future promotion campaigns based on historical data.

**Key Features:**
- Item similarity calculation
- Seasonality boost for same-month promotions
- Cold start handling for new product categories
- Hadoop-based data storage and processing
