# create a pdf document using Python

from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L,", ln=1)
    pdf.line(10, 21, 200, 21)

    # making lines
    for i in range(0, 270, 10):
        pdf.line(10, 21 + i, 200, 21 + i)

    # set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for page in range(1, row["Pages"]):
        pdf.add_page()

        # making lines
        for i in range(0, 270, 10):
            pdf.line(10, 21 + i, 200, 21 + i)

        # set the footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
pdf.output("output.pdf")
