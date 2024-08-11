import csv, time
from fpdf import FPDF

menu = {}                                   # This is were I'm taking the menu to be used in the Bill class.
with open ("./menu.csv") as csv_menu:       # Bringing here this dictionary I can have access to the price of any item by name.
    reader = csv.DictReader(csv_menu)
    for row in reader:
        menu[row["Item"]] = float(row["Price"].replace("$", ""))
 # I have to do the try except blocks to check the keys in the menu.csv file

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
            writer = csv.DictWriter(file, fieldnames= ["Customer name","Items", "Price", "Ordered at"]) 
            writer.writerow({"Customer name": self.customer_name, "Items": items, "Price": self.amount, "Ordered at": self.time_of_order})

    def tap(self, taxes):                   # This method is to check the current tap of each instance. It has taxes as parameter but then is
        tax = self.amount*taxes/100         # set to 19 %. Altought the tip will always be asked.
        tip = self.amount*int(input(f"Please enter the percentage {self.customer_name}'d like to tip: "))/100
        total = self.amount + tax + tip
        print(f"{self.customer_name} Here is your current bill:")
        for item in self.items:
            print(f"{item} ${menu[item]:,.2f}")
        print(f"Taxes: ${tax:,.2f}")
        print(f"Tip: ${tip:,.2f}")
        print(f"Total: ${total:,.2f}")

    def invoice(self, customer, tip_percentage):

        class PDF(FPDF):    # header and footer methos are called automatically, but we have to extend the class and override them.
            
            def header(self):
                self.image("./cs50_shirt.png", 10, 10, 20)                      # Rendering logo (path, position_x, position_y, width):
                self.set_font("helvetica", "B", 15)                             # Setting font: helvetica bold 15
                self.cell(50)                                                   # Moving cursor to the right:
                self.cell(100, 10, "__BADR__BAR__RESTAURANT__", border=0, align="C")         # Printing title:
                self.ln(20)                                                     # Performing a line break:
                self.set_font("helvetica", "B", 12)                             # Setting font: helvetica bold 15
                self.cell(20, 20, f"This is your invoice {customer}", border=0, align="L")
                self.ln(20)

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
        
        taxes = invoice_amount*0.19
        tip_amount = invoice_amount*tip_percentage/100
        
        invoice_pdf = PDF()
        invoice_pdf.set_font("helvetica", size=10)
        invoice_pdf.add_page()

        invoice_customer.insert(0, ["Customer name","Item(s)","Price [$]", "Ordered at"])

        with invoice_pdf.table() as table:
            for invoice_row in invoice_customer:
                row = table.row()
                for item in invoice_row:
                    row.cell(item)

        invoice_pdf.ln(20)
        invoice_pdf.set_font("helvetica", size=12)
        invoice_pdf.cell(0, 0, f"Tip: ${tip_amount:,.2f}", align="R")
        invoice_pdf.ln(7)
        invoice_pdf.cell(0, 0, f"Taxes: ${taxes:,.2f}", align="R")
        invoice_pdf.ln(7)
        invoice_pdf.set_font("helvetica","B", size=12)
        invoice_pdf.cell(0, 0, f"Total: ${invoice_amount+taxes+tip_amount:,.2f}", align="R")

        invoice_pdf.output(f"{customer}_bill.pdf")

    def delete_customer(self, customer_name):
        with open("./current_bills.csv") as file:
            all_taps = list(csv.DictReader(file))
            
        active_customers = [row for row in all_taps if row["Customer_name"] != customer_name]
        
        with open("./current_bills.csv", "w") as file:
            updated_taps = csv.DictWriter(file, fieldnames= ["Customer_name", "Items", "Price", "Ordered_at"])
            updated_taps.writeheader()
            updated_taps.writerows(active_customers)
          
