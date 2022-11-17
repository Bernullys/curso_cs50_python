def main():


    file = file_type(input("File name: "))

def file_type(a):

    file = a.casefold().strip()

    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

    return file

main()