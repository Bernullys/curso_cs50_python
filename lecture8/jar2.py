class Jar:

    def __init__(self, capacity=12, size=0):
        self._capacity = capacity
        self._size = size


    def __str__(self):
        cookies = self._size * "🍪"
        return f"{cookies}"


    def deposit(self, n):
        self.add = n
        if self.add + self._size <= self._capacity:
            self._size = n + self._size
        else:
            raise ValueError("Jar cannot hold that many!")


    def withdraw(self, n):
        self.substract = n
        if self._size - self.substract > 0:
            self._size -= self.substract
        else:
            raise ValueError("Jar has not that many!")


    @property
    def capacity(self):
        return self._capacity
        

    @property
    def size(self):
        self._size = self._size + self.deposit() - self.substract()


def main():

    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    print(jar)

if __name__=="__main__":
    main()


