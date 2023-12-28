import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^(\d\.|(\d){2}\.|1(\d){2}\.|2[0-4]\d\.){3}(\d\.|(\d){2}\.|1(\d){2}\.|2[0-4]\d\.)$", ip): #revisar
        return True
    else:
        return False


if __name__ == "__main__":
    main()