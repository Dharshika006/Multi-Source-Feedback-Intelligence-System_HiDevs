def detect_trends(df):

    trend = df["sentiment"].value_counts().to_dict()

    return trend