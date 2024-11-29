# Generate a printable version of bitwarden vault
# as a physical backup

import os
from fpdf import FPDF

def output(file_name: str):
    path = "./output"
    if not os.path.exists(path):
        os.mkdir(path)
    pdf.output(f"{path}/{file_name}")

pdf = FPDF(format="Letter")
pdf.add_page()
pdf.set_margins(25.4, 25.4, 25.4)
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Bitwarden")
pdf.cell(40, 10, "next")
output("tuto1.pdf")
