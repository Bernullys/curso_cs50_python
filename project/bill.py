import csv, time
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode


menu = {}                                   # This is were I'm taking the menu to be used in the Bill class.
with open ("./menu.csv") as csv_menu:       # Bringing here this dictionary I can have access to the price of any item by name.
    reader = csv.DictReader(csv_menu)
    for row in reader:
        menu[row["item"]] = float(row["price"])
 

class Bill:                                 # With this class I'm creating customers by name and adding the items to their order list.
    def __init__(self, customer_name):      # Here I'm passing as a name when instancieate a Bill class.
        self.customer_name = customer_name
        self.items = []                     # Here I'm initializating an empty list where will be append the orders of each intance.
        self.amount = 0                     # Here will contain the sum of costs by orders.
    
    def order(self, items):                 # This method will be used every time a instancie oreder an item. Items has to be in the menu.
        self.items.append(items)            # Ass the items are in the menu, its value is the price which will be sum in amount property.
        self.amount += menu[items]
        self.time_of_order = time.asctime() # Time is usefull to get record and remember exactly when the order was made.
               
        with open ("./current_bills.csv", "a") as file:     # This part is to save every order into a csv file so in case of closing the app,
                                                            # the  orders will still remain saved and also to print the customer pdf invoice.
            writer = csv.DictWriter(file, fieldnames= ["customer name","items", "price", "ordered at"]) 
            writer.writerow({"customer name": self.customer_name, "items": items, "price": self.amount, "ordered at": self.time_of_order})

    def tap(self, taxes):                   # This method is to check the current tap of each instance. It has taxes as parameter but then is
        tax = self.amount*taxes/100         # set to 10%. Altought the tip will always be asked.
        tip = self.amount*int(input("Please type how much will be your % tip: "))/100
        total = self.amount + tax + tip
        print(f"{self.customer_name} this is your current bill:")
        for item in self.items:
            print(f"{item}              {menu[item]} order on {self.time_of_order}")
        print(f"Taxes:              {tax}")
        print(f"Tip:                {tip}")
        print(f"Total:              {total}")

    def invoice(self, customer, tip_percentage):

        class PDF(FPDF):    # header and footer methos are called automatically, but we have to extend the class and override them.
            
            def header(self):
                self.image("./cs50_shirt.png", 10, 10, 20)                      # Rendering logo (path, position_x, position_y, width):
                self.set_font("helvetica", "B", 15)                             # Setting font: helvetica bold 15
                self.cell(80)                                                   # Moving cursor to the right:
                self.cell(30, 10, "__BADR__BAR__", border=0, align="C")         # Printing title:
                self.ln(50)                                                     # Performing a line break:

            def footer(self):
                self.set_y(-15)                                                 # Position cursor at 1.5 cm from bottom:
                self.set_font("helvetica", "I", 8)                              # Setting font: helvetica italic 8
                self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")    # Printing page number:

        with open("./current_bills.csv") as taps:                                   # Here we read the csv file with all the items of every customer.
            invoices = list(csv.reader(taps))                                       # Here we are making a list with all the rows of the csv file.
            invoice_amount = 0                                                      # Here we initialized the amount to 0.
            for row in invoices:
                invoice_customer = [row for row in invoices if row[0] == customer]  # Here we check if the customer name's match with the type to
                if row[0] == customer:                                              # print its invoice.
                    invoice_amount += float(row[2])                                 # Now we add the amount of items of that customer.
        
        taxes = invoice_amount*1.19
        tip_amount = invoice_amount*tip_percentage
        invoice_pdf = PDF()
        invoice_pdf.set_font("helvetica", size=14)
        invoice_pdf.add_page()

        with invoice_pdf.table() as table:
            for invoice_row in invoice_customer:
                row = table.row()
                for item in invoice_row:
                    row.cell(item)

        invoice_pdf.ln(50)
        invoice_pdf.set_font("helvetica", size=14)
        invoice_pdf.cell(0, 0, f"This is Total: {invoice_amount}")
        invoice_pdf.ln(20)
        invoice_pdf.cell(0, 0, f"Taxes: {taxes}")
        invoice_pdf.ln(20)
        invoice_pdf.cell(0, 0, f"Tip: {tip_amount}")

        print(f"Thank's {customer} for your purchase, your invoice has been printed as a pdf. Please come back soon! Bye")
        invoice_pdf.output(f"{customer}_bill.pdf")

    def delete_customer(self, customer_name):
        with open("./current_bills.csv") as file:
            all_taps = list(csv.DictReader(file))
            
        active_customers = [row for row in all_taps if row["customer_name"] != customer_name]
        
        with open("./current_bills.csv", "w") as file:
            updated_taps = csv.DictWriter(file, fieldnames= ["customer_name", "items", "price", "ordered_at"])
            updated_taps.writeheader()
            updated_taps.writerows(active_customers)
          
