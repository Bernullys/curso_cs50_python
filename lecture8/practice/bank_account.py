class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
        self.log = [self.balance]
    
    def deposit(self, depo):
        self.balance += depo
        self.log.append(f"+ {depo}")
        return self.balance
    
    def withdraw(self, withd):
        self.balance -= withd
        self.log.append(f"- {withd}")
        return self.balance
        


person = BankAccount(100, "Bernardo")
print(person.owner, person.balance)

person.deposit(100)
person.withdraw(50)
for log in person.log:
    print(log)
print(person.balance)