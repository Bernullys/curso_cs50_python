import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        try:
            if level < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            break

real_level = level + 1
rang = list(range(real_level))
randon_choice = random.choice(rang)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        try:
            if guess <= 0:
                raise TypeError
        except TypeError:
            pass
        else:
            if guess > randon_choice:
                print("Too large!")
            elif guess < randon_choice:
                print("Too small!")
            else:
                print("Just right!")
                break


