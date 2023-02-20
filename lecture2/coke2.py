coke_value = print("Amount Due: 50")
amount_due = 50
valid_coins = [5, 10, 25]

while amount_due > 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in valid_coins:
        amount_due -= insert_coin
        if amount_due > 0: print("Amount Due: ", amount_due)
        elif amount_due <= 0: print("Change Owed: ",abs(amount_due))
    else: print("Amount Due: 50")