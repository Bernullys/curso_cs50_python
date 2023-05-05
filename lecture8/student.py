class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name cannot be empty")
        if house not in ["Chile", "Depto", "610"]:
            raise ValueError("House must be Chile, Depto or 610")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "image.png"
            case "Otter":
                return "😎"
            case "dog":
                return "🐶"
            case _:
                return "☁️"


def main():
    student = get_student()
    print("Expecto Patronum")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)  #this is a constructor



if __name__=="__main__":
    main()