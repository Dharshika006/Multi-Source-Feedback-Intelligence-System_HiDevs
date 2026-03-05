def categorize(text):

    text = text.lower()

    if "crash" in text or "bug" in text:
        return "Bug"

    if "slow" in text:
        return "Performance"

    if "feature" in text:
        return "Feature Request"

    return "General"