import random

def main():

    level = get_level()

    i_times = 1
    score = 0

    while i_times <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        user_answer = simulate_attemps(x,y)
        if user_answer == True:
            score += 1
        i_times += 1

    print(f"Score: {score}")

def get_level():
    while True:                             # Another way:
        try:                      
            level = int(input("Level: "))   
            if level > 0 and level <= 3:    #   if level in [1,2,3]:
                return level                #       break
        except ValueError:                  # except:
            pass                            #   pass
                                            # return level   
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:                        # else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x                                # return x,y
    return y

def simulate_attemps(x,y):
    attemps = 1
    while attemps <= 3:
        try:
            users_answer = int(input(f"{x} + {y} = "))
            if users_answer == (x+y):
                return True
            else:
                attemps += 1
                print("EEE")
        except ValueError:
            attemps += 1
            print("EEE")    
    print(f"{x} + {y} = {x+y}")
    return False


if __name__ == "__main__":
    main()