class Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    #Getter
    @property
    def house(self):
        return self._house
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Chile", "depto", "610"]:
            raise ValueError("Invalid house")
        self._house = house

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  #this is a constructor



if __name__=="__main__":
    main()