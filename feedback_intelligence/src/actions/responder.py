def suggest_response(sentiment):

    if sentiment == "Negative":
        return "We apologize for the issue and will improve soon."

    if sentiment == "Positive":
        return "Thank you for the positive feedback."

    return "Thanks for sharing your thoughts."