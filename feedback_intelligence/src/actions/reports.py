import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_chart(trend):

    labels = list(trend.keys())
    values = list(trend.values())

    plt.bar(labels, values)
    plt.title("Sentiment Distribution")
    plt.savefig("sentiment_chart.png")
    plt.close()

def generate_report(trend, insight):

    generate_chart(trend)

    doc = SimpleDocTemplate("feedback_report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Feedback Intelligence Report", styles["Title"]))

    for k,v in trend.items():
        content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    content.append(Paragraph(f"Insight: {insight}", styles["Normal"]))

    content.append(Image("sentiment_chart.png"))

    doc.build(content)