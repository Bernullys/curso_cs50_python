from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode
import csv

# class PDF(FPDF):
#     def header(self):
#         self.image("./cs50_shirt.png", 10, 10, 40)
#         self.set_font("helvetica", "B", 16)
#         self.cell(80)
#         self.cell(30, 10, "Factura N° xxxx", border=1, align="C")
#         self.ln(50)

#     def footer(self):
#         self.set_y(280)
#         self.set_font("helvetica", "I", 8)
#         self.cell(0, 0, "Thanks for your confidance", align="C")
#         self.ln(8)
#         self.cell(0, 0, f"Page {self.page_no()}/{{nb}}", align="C")

# bill_print = PDF()
# bill_print.add_page()

with open("./current_bills.csv") as csv_file:
    data = list(csv.reader(csv_file))
    for row in data:
        invoice_costumer = [row for row in data if row[0] == "Ber"]

pdf = FPDF()
pdf.set_font("helvetica", size=14)
pdf.add_page()

headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 100))

with pdf.table(
    borders_layout="NO_HORIZONTAL_LINES",
    cell_fill_color=(224, 235, 255),
    cell_fill_mode=TableCellFillMode.ROWS,
    col_widths=(42, 39, 35, 42),
    headings_style=headings_style,
    line_height=6,
    text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
    width=160,
) as table:
    for data_row in invoice_costumer:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("bill_1.pdf")
