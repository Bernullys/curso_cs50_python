class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        if house not in ["Chile", "Depto", "610"]:
            raise ValueError("House must be Chile, Depto or 610")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    #Getter
    def house(self):
        return self.house
    #Setter
    def house(self, house):
        return self.house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  #this is a constructor



if __name__=="__main__":
    main()