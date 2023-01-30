# This program get a string as an input and then change it to a lower case, like is talking indoor.
# Also can get it with spaces before the message using strip.

# I changed the code. Now Is using a function to run.

def main():

    message = input("")
    low_voice = indoor(message)
    print(low_voice)

def indoor(message):
    low_voice = message.strip().lower()
    return low_voice

main()