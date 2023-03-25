import random

def main():

    level = get_level()

    i = 1
    score = 0
    while i <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        print(x, " + ", y, " = ", end="")
        users_answer = int(input())
        answer = x+y
        if users_answer == answer:
            score += 1
        elif users_answer != answer:
            print("EEE")
            attemps = 2
            while users_answer != answer:
                while attemps <= 3:
                    print(x, " + ", y, " = ", end="")
                    users_answer = int(input())
                    if users_answer == answer:
                        score += 1
                        break
                    else:
                        attemps += 1
                    print("EEE")
                print(x, " + ", y, " = ",answer)
                break
        i += 1

    print(score)

def get_level():
    while True:
        try:     
            level = int(input("Level: "))
            if level > 0 and level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x
    return y

if __name__ == "__main__":
    main()