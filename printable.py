# Generate a printable version of bitwarden vault
# as a physical backup

import os
import json
import argparse
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=16)
        self.cell(40, 10, "Bitwarden")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", style="I", size=8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def gen_output(self, file_name: str):
        path = "output"
        if not os.path.isdir(path):
            os.mkdir(path)
        self.output(f"{path}/{file_name}")

# Get cmd args
parser = argparse.ArgumentParser(description="Generate readable printout from Bitwarden JSON")
parser.add_argument('filename')
args = parser.parse_args()

# Parse JSON file
filename = args.filename
with open(filename, 'r') as file:
    data = json.load(file)


# Define PDF object
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)

for item in data["items"]:
    pdf.cell(0, 10, item["name"], new_x="LMARGIN", new_y="NEXT")
pdf.gen_output("test3.pdf")
