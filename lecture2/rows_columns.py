def main():

    print_square(5)

def print_square(size):

    # For each row in square

    for i in range(size):

        # Print brick in row

        for j in range(size):

            #Print brick

            print("#", end="")
        
        # Print blanck line

        print()

main()