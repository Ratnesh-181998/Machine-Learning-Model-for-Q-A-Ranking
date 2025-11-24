# Machine Learning Model for Q&A Ranking

A comprehensive implementation of ML systems for Q&A ranking and promotion forecasting, designed for platforms like Quora, Reddit, and e-commerce sites.

## 🚀 Quick Start

### Running Q&A Ranking
```bash
cd examples
python run_qa_ranking.py
```

### Running Promotion Forecasting
```bash
cd examples
python run_promotion_forecasting.py
```

## 📁 Project Structure

```
.
├── qa_ranking/              # Q&A Ranking System
│   └── qa_ranker.py        # Core ranking logic
├── promotion_forecasting/   # Promotion Forecasting System
│   └── promo_forecaster.py # Core forecasting logic
├── examples/                # Example usage scripts
│   ├── run_qa_ranking.py
│   └── run_promotion_forecasting.py
├── notes.md                 # Detailed technical notes
├── README.md
└── LICENSE
```

## 🎯 Features

### Q&A Ranking System
- **Text Similarity**: Jaccard-based semantic matching
- **Interaction Metrics**: Upvotes, CTR, impressions
- **Quality Filtering**: Spam detection for short/low-quality answers
- **Scalability**: Designed for millions of Q&A pairs with <100ms latency

**Example:**
```python
from qa_ranking.qa_ranker import QARankingSystem

ranker = QARankingSystem()
question = "What is machine learning?"
answers = [
    {"text": "ML is a subset of AI...", "upvotes": 100, "impressions": 500},
    {"text": "I don't know", "upvotes": 0, "impressions": 10}
]
ranked = ranker.rank_answers(question, answers)
```

### Promotion Forecasting System
- **Item Similarity**: Coverage-based matching (|A ∩ B| / |B|)
- **Seasonality Boost**: 20% boost for same-month promotions
- **Cold Start Handling**: Fallback to historical averages
- **Data Architecture**: Designed for Hadoop/NoSQL storage

**Example:**
```python
from promotion_forecasting.promo_forecaster import PromotionForecaster

forecaster = PromotionForecaster()
items = ["iphone14", "samsung_s23", "macbook"]
predicted_sales, details = forecaster.predict_sales(items, "2025-06-15")
```

## 📊 Evaluation Metrics

### Q&A Ranking
- **Offline**: NDCG, MRR, F1-Score, AUC
- **Online**: Click-Through Rate (CTR), A/B Testing

### Promotion Forecasting
- **Accuracy**: MAPE, RMSE
- **Business Metrics**: Revenue impact, forecast vs. actual

## 🛠️ Technical Details

### Q&A Ranking Algorithm
1. **Text Processing**: Tokenization, lowercasing, punctuation removal
2. **Similarity Calculation**: Jaccard index between question and answer
3. **Scoring Formula**: 
   ```
   Score = 0.6 × Similarity + 2.0 × CTR + 0.1 × log(Upvotes + 1) + Penalty
   ```
4. **Quality Filter**: -0.5 penalty for answers with <5 words

### Promotion Forecasting Algorithm
1. **Item Similarity**: `Similarity = |Historical_Items ∩ Current_Items| / |Current_Items|`
2. **Seasonality**: +0.2 boost if promotion month matches historical month
3. **Cold Start**: Use average of all historical sales if similarity = 0

## 📚 Use Cases

### Q&A Platforms
- **Quora**: Rank answers to maximize user engagement
- **Reddit**: Sort comments by relevance
- **Stack Overflow**: Prioritize helpful answers

### E-commerce
- **Amazon**: Forecast promotion performance
- **Flipkart**: Plan seasonal campaigns
- **Walmart**: Optimize inventory for promotions

## 🔧 Requirements
- Python 3.7+
- No external dependencies (uses only standard library)

## 📖 Documentation
See [notes.md](notes.md) for detailed technical documentation including:
- System design considerations
- Feature engineering strategies
- Model selection rationale
- Deployment architecture

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact
For questions or feedback, please open an issue on GitHub.
