from google_play_scraper import reviews
import pandas as pd

def fetch_play_reviews(app_id):

    result, _ = reviews(app_id, count=50)

    data = []

    for r in result:
        data.append({
            "text": r["content"],
            "rating": r["score"],
            "source": "playstore"
        })

    return pd.DataFrame(data)