def prioritize_issues(df):

    issues = df[df["sentiment"] == "Negative"]

    counts = issues["category"].value_counts()

    return counts.to_dict()