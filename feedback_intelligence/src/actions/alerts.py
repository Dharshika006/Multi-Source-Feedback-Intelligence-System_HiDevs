def check_and_alert(trend):

    negative = trend.get("Negative",0)

    if negative >= 5:
        print("ALERT: Negative feedback spike detected")