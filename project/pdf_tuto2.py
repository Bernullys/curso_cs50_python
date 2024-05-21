from fpdf import FPDF


class PDF(FPDF):
    # header and footer methos are called automatically, but we have to extend the class and override them.
    def header(self):
        # Rendering logo (path, position_x, position_y, width):
        self.image("./cs50_shirt.png", 10, 10, 20)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(50)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 111):
    # if the text is longer than the width of the page -- is going to be print outside the page
    pdf.cell(0, 20, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
pdf.output("tuto_2.pdf")