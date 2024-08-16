from bill import Bill

customer1 = Bill("Bernardo")
customer2 = Bill("Jestin")
customers = [customer1, customer2]

customers_names = [customer.customer_name for customer in customers]

print(customers_names)