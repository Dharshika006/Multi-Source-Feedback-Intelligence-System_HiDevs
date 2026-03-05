from textblob import TextBlob

def sentiment_analysis(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "Positive", polarity

    elif polarity < -0.1:
        return "Negative", polarity

    else:
        return "Neutral", polarity