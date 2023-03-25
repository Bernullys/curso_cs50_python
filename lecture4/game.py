import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            myError = ValueError
            raise myError
    except (ValueError):
        pass
    else:    
        break

random_output = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            my_error = ValueError
            raise my_error
    except (ValueError):
        pass
    else:
        if random_output > guess:
            print("Too small!")
        elif random_output < guess:
            print("Too large!")
        else:
            break
print("Just right!")

    