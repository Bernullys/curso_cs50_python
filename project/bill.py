import csv, time
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode


menu = {}                                   # This is were I'm taking the menu to be used in the Bill class.
with open ("./menu.csv") as csv_menu:       # Bringing here this dictionary I can have access to the price of any item by name.
    reader = csv.DictReader(csv_menu)
    for row in reader:
        menu[row["item"]] = float(row["price"])
 

class Bill:                                 # With this class I'm creating costumers by name and adding the items to their order list.
    def __init__(self, custumer_name):      # Here I'm passing as a name when instancieate a Bill class.
        self.custumer_name = custumer_name
        self.items = []                     # Here I'm initializating an empty list where will be append the orders of each intance.
        self.amount = 0                     # Here will contain the sum of costs by orders.
    
    def order(self, items):                 # This method will be used every time a instancie oreder an item. Items has to be in the menu.
        self.items.append(items)            # Ass the items are in the menu, its value is the price which will be sum in amount property.
        self.amount += menu[items]
        self.time_of_order = time.asctime() # Time is usefull to get record and remember exactly when the order was made.
               
        with open ("./current_bills.csv", "a") as file:     # This part is to save every order into a csv file so in case of closing the app,
                                                            # the  orders will still remain saved and also to print the costumer pdf invoice.
            writer = csv.DictWriter(file, fieldnames= ["custumer name","items", "price", "ordered at"]) 
            writer.writerow({"custumer name": self.custumer_name, "items": items, "price": self.amount, "ordered at": self.time_of_order})

    def tap(self, taxes):                   # This method is to check the current tap of each instance. It has taxes as parameter but then is
        tax = self.amount*taxes/100         # set to 10%. Altought the tip will always be asked.
        tip = self.amount*int(input("Please type how much will be your % tip: "))/100
        total = self.amount + tax + tip
        print(f"{self.custumer_name} this is your current bill:")
        for item in self.items:
            print(f"{item}              {menu[item]} order on {self.time_of_order}")
        print(f"Taxes:              {tax}")
        print(f"Tip:                {tip}")
        print(f"Total:              {total}")

    def invoice(self, costumer):

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

        with open("./current_bills.csv") as taps:
            invoices = list(csv.reader(taps))
            for row in invoices:
                invoice_costumer = [row for row in invoices if row[0] == costumer]
        invoice_pdf = PDF()
        invoice_pdf.set_font("helvetica", size=14)
        invoice_pdf.add_page()
        #headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 100))
        # with invoice_pdf.table(
        #     borders_layout="NO_HORIZONTAL_LINES",
        #     cell_fill_color=(224, 235, 255),
        #     cell_fill_mode=TableCellFillMode.ROWS,
        #     col_widths=(42, 39, 35, 42),
        #     headings_style = headings_style,
        #     line_height=6,
        #     text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
        #     width=160,
        #     ) as table:
        #     for data_row in invoice_costumer:
        #         row = table.row()
        #         for datum in data_row:
        #             row.cell(datum)
        with invoice_pdf.table() as table:
            for invoice_row in invoice_costumer:
                row = table.row()
                for d in invoice_row:
                    row.cell(d)

        invoice_pdf.output("bill_1.pdf")
