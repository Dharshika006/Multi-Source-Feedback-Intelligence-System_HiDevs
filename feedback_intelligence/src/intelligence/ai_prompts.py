def generate_business_insight(trend):

    positive = trend.get("Positive", 0)
    negative = trend.get("Negative", 0)

    if negative > positive:
        return "⚠ Negative feedback increasing. Immediate attention required."

    return "✅ Customer sentiment is healthy."