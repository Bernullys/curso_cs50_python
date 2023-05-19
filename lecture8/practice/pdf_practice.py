
from fpdf import FPDF

class PDF(FPDF):                                                    #Cualquier clase creada hija de FPDF
    def header(self):
        self.image("./shirtificate.png", 15, 80, 180)               # los numeros son: posición x, posiciín y, tamaño
        self.set_font("helvetica", "B", 45)                         # set the font (it has to be set)
        self.cell(200, 50, "CS50 Shirtificate", align="C")          # prints a cell width, height (a rectangle area wich contains text)



pdf = PDF()                                                         # se crea el objeto pdf de clase PDF with default values (clase hija de FPDF)
pdf.add_page()                                                      # adds a page
pdf.set_font("courier", "B", 35)
pdf.set_text_color(255,255,255)                                  
name = input("Name: ")
pdf.cell(-210, 250, name, align="C") 
pdf.output("shirtificate.pdf")                                      # saves a file with the name and extension