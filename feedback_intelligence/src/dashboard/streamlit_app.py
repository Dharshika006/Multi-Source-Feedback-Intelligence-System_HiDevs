import streamlit as st
import requests
import pandas as pd

st.title("Feedback Intelligence Dashboard")

st.write("Analyze customer feedback and detect trends")

API_URL = "http://127.0.0.1:8000/analyze"

if st.button("Run Feedback Analysis"):

    response = requests.get(API_URL)

    if response.status_code == 200:

        data = response.json()

        trend = data["trend"]
        issues = data["priority_issues"]
        negatives = data["top_negative_reviews"]
        keywords = data["trending_keywords"]
        weekly = data["weekly_sentiment"]

        # Sentiment Chart
        st.subheader("Sentiment Distribution")

        trend_df = pd.DataFrame(
            list(trend.items()),
            columns=["Sentiment", "Count"]
        )

        st.bar_chart(trend_df.set_index("Sentiment"))

        # Weekly Trend
        st.subheader("Weekly Sentiment Trend")

        weekly_df = pd.DataFrame(weekly)

        if not weekly_df.empty:

            pivot = weekly_df.pivot(
                index="date",
                columns="sentiment",
                values="count"
            )

            st.line_chart(pivot)

        # Priority Issues
        st.subheader("Priority Issues")

        issues_df = pd.DataFrame(
            list(issues.items()),
            columns=["Category", "Count"]
        )

        st.table(issues_df)

        # Top Negative Reviews
        st.subheader("Top Negative Reviews")

        for review in negatives:
            st.warning(review)

        # Trending Keywords
        st.subheader("Trending Keywords")

        keyword_df = pd.DataFrame(
            keywords,
            columns=["Keyword", "Frequency"]
        )

        st.table(keyword_df)

        st.success("Analysis Completed")

    else:
        st.error("API connection failed")