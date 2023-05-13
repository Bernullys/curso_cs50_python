class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("La capacidad no puede ser negativa")
        #self.capacity = capacity
    
    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        self.deposit = n
        return self.deposit

    def withdraw(self):
        ...

    @property
    def capacity(self):
        return self.capacity
    
    @property
    def size(self):
        self.size = self.deposit
        return self.size

jarra = Jar()
jarra.deposit(3)
print(jarra.size())



