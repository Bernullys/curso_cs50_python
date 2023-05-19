class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("La capacidad no puede ser negativa")
        self._capacity = capacity
        self._size = 0
    
    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("No caben tantas galletas")
        elif self._size + n > self.capacity:
            raise ValueError("No caben tantas galletas")
        self.deposit = n
        self._size += n

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self._size < self.withdraw:
            raise ValueError("No hay tantas galletas")
        self._size -= self.withdraw

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size

jarra = Jar()
print(jarra.capacity)
jarra.deposit(4)
print(jarra)
jarra.withdraw(3)
print(jarra)
print(jarra.size)
