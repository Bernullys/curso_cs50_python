class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("La capacidad no puede ser negativa")
        self._capacity = capacity
        self.size = 0
    
    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("No caben tantas galletas")
        elif self.size + n > self.capacity:
            raise ValueError("No caben tantas galletas")
        self.deposit = n
        self.size += n

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self.size < self.withdraw:
            raise ValueError("No hay tantas galletas")
        self.size -= self.withdraw

    @property
    def capacity(self):
        return self._capacity
    
    # @property
    # def size(self):
    #     return self._size

jarra = Jar()
jarra.capacity = 3
print(jarra.capacity)

# jarra.capacity(5)
# jarra.deposit(4)
# print(jarra)
# print(jarra.deposit)
# jarra.withdraw(3)
# print(jarra.withdraw)
# print(jarra)
