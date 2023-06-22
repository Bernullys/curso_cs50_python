import validators

asking_email = input("What's your email address? ")

if validators.email(asking_email):
    print("Valid")
else:
    print("Invalid")