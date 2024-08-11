from fpdf import FPDF
#Orientarion options: P for portrait, L for lanscape

#Create FPDF object
#Layout ("P", "L")
#Unit ("mm", "cm", "in")
#Format ("A3", "A4"(default), "A5", "Letter", "Legal", (100,150))
pdf = FPDF(orientation = "P", unit= "mm", format="A4")
# Add a page
pdf.add_page()

# Specify font
# Fonts ("times", "Courier", "helvetica", "symbol", "zpfdingbats")
# "B" (bold), "U" (underline), "I" (italics), "" (regular), combination(i.e., ("BU"))
pdf.set_font("helvetica", "B", 16)

# Add text
# w = width
# h = height
# txt = your text
# border True or False
# ln () (move cursor down to next line)
pdf.cell(180, 20, "Hello world", border=True)
pdf.ln(50)
pdf.cell(80, 30, "Hello world2", True)
pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')

pdf.output("tuto_1.pdf")