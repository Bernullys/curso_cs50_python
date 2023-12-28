import random

def main():
    n = get_level()
    score = 0
    i = 0
    while i < 10:
        x, y  = generate_integer(n)
        correct_answer = x + y
        user_answer = int(input(f"{x} + {y} = "))
        if user_answer == correct_answer:
            score += 1
        else:
            trys = 1
            print("EEE")
            while trys < 3:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer!= correct_answer:
                    trys += 1
                    print("EEE")
                    if trys == 3:
                        print(correct_answer)
                else:
                    score += 1
                    break
        i += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in list(range(1,4)):
                raise ValueError ("Level should be 1, 2 or 3")
        except ValueError:
            pass
        else:
            return level
            break

def generate_integer(level):
    if level not in list(range(1,4)):
        raise ValueError ("Level should be 1, 2 or 3")
    else:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        return (x, y)

if __name__ == "__main__":
    main()