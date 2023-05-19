import sys

def main():

    exact_input()
    lines = []
    with open(sys.argv[1]) as file:
        for line in file:
            #Exclude comments
            #Exclude blank lines
            if line.startswith("#") or line.rstrip() == "":
                lines = lines
            else:
                lines.append(line.rstrip())
    print(len(lines))

def exact_input():

    #Less than one command-line argument should say: Too few command line arguments
    #More than one command-line argument should say: Too many command line arguments
    #If the file under test does not ends with .py should say: Not a python file
    #If the file under test does not exist - should say: File does not exist

    if len(sys.argv) < 3:
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        return sys.exit("Too many command-line arguments")
    # elif sys.argv[1].endswith(".py") == False:
    #     return sys.exit("Not a Python file")
    elif sys.argv[1].endswith(".csv") == False:
        return sys.exit("Not a CSV file")
    else:
        try:
            open(sys.argv[1])
        except FileNotFoundError:
            return sys.exit("File does not exist")

if __name__=="__main__":
    main()