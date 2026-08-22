with open("Create.txt", "w") as f :
    f.write("Hello World")

with open("Create.txt",) as f:
    print(f.read())