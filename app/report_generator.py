from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_report(
    filename,
    time_site,
    age,
    income,
    internet,
    gender,
    prediction,
    probability
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AdVision-AI</b>", styles["Title"]))

    story.append(
        Paragraph(
            "Advertisement Click Prediction Report",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y %I:%M %p')}",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Customer Information</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(f"Age : {age}", styles["Normal"])
    )

    story.append(
        Paragraph(f"Gender : {gender}", styles["Normal"])
    )

    story.append(
        Paragraph(f"Area Income : ${income}", styles["Normal"])
    )

    story.append(
        Paragraph(
            f"Daily Time on Site : {time_site} minutes",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Daily Internet Usage : {internet} minutes",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Prediction</b>", styles["Heading2"])
    )

    result = (
        "Likely to Click Advertisement"
        if prediction == 1
        else
        "Unlikely to Click Advertisement"
    )

    story.append(
        Paragraph(result, styles["Normal"])
    )

    story.append(
        Paragraph(
            f"Probability : {probability*100:.2f}%",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Business Recommendation</b>", styles["Heading2"])
    )

    if prediction == 1:

        recommendation = """
        • Premium Campaigns<br/>
        • Personalized Advertisements<br/>
        • Retarget Existing Customers
        """

    else:

        recommendation = """
        • Awareness Campaigns<br/>
        • Discount Offers<br/>
        • Social Media Marketing
        """

    story.append(
        Paragraph(recommendation, styles["Normal"])
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Model Used</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            "Logistic Regression",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>Developer</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Vanshika Rathore",
            styles["Normal"]
        )
    )

    doc.build(story)