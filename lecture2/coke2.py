def main():

    coke_type = int(input("Coke Type: "))
    prices_per_type = [5, 10, 15, 25, 30, 50]
    if coke_type in prices_per_type:
        print("Amount Due: $",coke_type)
        coke_machine(coke_type)
    else: print("Selec a correct type")
    
def coke_machine(coke_type):
    
    amount_due = coke_type
    valid_coins = [5, 10, 25]
    while amount_due > 0:
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in valid_coins:
            amount_due -= insert_coin
            if amount_due > 0: print("Amount Due: ", amount_due)
            elif amount_due <= 0: print("Change Owed: ",abs(amount_due))
        else: print("Amount Due: ",amount_due)

main()