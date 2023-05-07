class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        self.house = house

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        self.subject = subject


def main():
    student = Student.get()
    print(student)


if __name__=="__main__":
    main()