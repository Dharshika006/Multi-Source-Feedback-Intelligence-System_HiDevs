from fastapi import APIRouter
import pandas as pd
from collections import Counter
import datetime

from feedback_intelligence.src.ingestion.playstore import fetch_play_reviews
from feedback_intelligence.src.processing.cleaner import clean_text
from feedback_intelligence.src.processing.analyzer import sentiment_analysis
from feedback_intelligence.src.processing.categorizer import categorize
from feedback_intelligence.src.intelligence.trend_detector import detect_trends
from feedback_intelligence.src.intelligence.prioritizer import prioritize_issues
from feedback_intelligence.src.actions.reports import generate_report

router = APIRouter()


@router.get("/analyze")
def analyze_feedback():

    # Fetch reviews
    reviews_data = fetch_play_reviews()

    data = pd.DataFrame(reviews_data)

    # Clean text
    data["clean"] = data["text"].apply(clean_text)

    # Sentiment
    sentiments = data["clean"].apply(sentiment_analysis)
    data["sentiment"] = sentiments.apply(lambda x: x[0])

    # Category
    data["category"] = data["clean"].apply(categorize)

    # Sentiment trend
    trend = detect_trends(data)

    # Priority issues
    issues = prioritize_issues(data)

    # Top negative reviews
    negative_reviews = data[data["sentiment"] == "Negative"]["text"].head(5).tolist()

    # Trending keywords
    words = " ".join(data["clean"]).split()
    keywords = Counter(words).most_common(10)

    # Weekly sentiment
    today = datetime.date.today()
    data["date"] = today

    weekly = data.groupby(["date", "sentiment"]).size().reset_index(name="count")

    insight = "Customer sentiment is healthy."

    # Generate PDF report
    generate_report(trend, insight)

    return {
        "trend": trend,
        "priority_issues": issues,
        "top_negative_reviews": negative_reviews,
        "trending_keywords": keywords,
        "weekly_sentiment": weekly.to_dict(orient="records"),
        "status": "analysis complete"
    }