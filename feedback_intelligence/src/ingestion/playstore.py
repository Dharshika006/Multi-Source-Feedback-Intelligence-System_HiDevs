from google_play_scraper import reviews

def fetch_play_reviews(app_id="com.instagram.android", count=50):

    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        count=count
    )

    feedback = []

    for r in result:
        feedback.append({
            "text": r["content"],
            "rating": r["score"]
        })

    return feedback