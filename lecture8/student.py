class Student:
    ...                 #this means later will be some code here

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()     #declaring student. is like calling a function
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__=="__main__":
    main()