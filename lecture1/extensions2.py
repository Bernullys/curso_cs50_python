f_n = input("File name: ").strip().lower()

if f_n.endswith(".gif"):
    print("image/gif")
elif f_n.endswith(".jpg"):
    print("image/jpeg")
elif f_n.endswith(".jpeg"):
    print("image/jpeg")
elif f_n.endswith(".png"):
    print("image/png")
elif f_n.endswith(".pdf"):
    print("application/pdf")
elif f_n.endswith(".txt"):
    print("text/plain")
elif f_n.endswith(".zip"):
    print("application/zip")
else: print("application/octetstream")
    