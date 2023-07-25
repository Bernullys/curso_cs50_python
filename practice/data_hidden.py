class Queue:
    def __init__(self, contents):
        self._hiddentlist = list(contents)

    def push(self, value):
        self._hiddentlist.insert(0, value)

    def pop(self):
        return self._hiddentlist.pop(-1)
    
    def __repr__(self):
        return "Queue({})".format(self._hiddentlist)

queue = Queue([1, 2, 3])
print(queue._hiddentlist)
print (queue)

queue.push(0)
print(queue)

queue.pop()
print(queue)

print(queue._hiddentlist)


###################################################

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)  #asi se puede acceder, incluyendo _ y el nombre de la clase.
##print(s.__egg)    #asi no se puede acceder.


####################################################

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives
    
    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")

p = Player("Bernardo", 3)
p.hit()
p.hit()
p.hit()