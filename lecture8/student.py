class Wizard:
    def __init__(self, name):
        super().__init__(name)
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# def main():
#     student = Student.get()
#     print(student)

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor(">Severus", "Defense against the dark arts")


if __name__=="__main__":
    main()