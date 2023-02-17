
coke_value = print("Amount Due: 50")

amount_due = 50

coins_accepts = [25, 10, 5]

coin_in = int(input("Insert Coin: "))

if coin_in in coins_accepts:
    
    while amount_due > 0:
        amount_due = amount_due - coin_in
        print("Amount Due:", amount_due)
        coin_in = int(input("Insert Coin: "))
    if amount_due == 0:
        print("Change Owed:", amount_due)

else: print("Amount Due: ")