def main():

    print("Amount Due: 50")
    coke_machine()
    

def coke_machine():

    amount_due = 50
    legal_coins = [5, 10, 25]

    while amount_due > 0:

        coin_inserted = int(input("Insert coin: "))

        if coin_inserted in legal_coins:

            amount_due -= coin_inserted

            if amount_due > 0:

                print(f"Amount Due: {amount_due}")

            elif amount_due <= 0:

                change_owed = abs(amount_due)
                print(f"Change Owed: {change_owed}")

        else:
            print(f"Amount Due: {amount_due}")

main()

