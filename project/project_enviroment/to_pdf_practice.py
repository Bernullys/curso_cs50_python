from fpdf import FPDF
#Orientarion options: P for portrait, L for lanscape

pdf = FPDF(orientation = "P", unit= "mm", format="A4")
pdf.add_page()
pdf.output("Sheet.pdf")