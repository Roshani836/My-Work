search_student = input("Enter the student name: ")

file = open("Create.txt" , "r")

found= False

for name in file:
    if name.strip().lower() == search_student.lower():
        found = True
        break

file.close()

if found:
    print("Studemt Found")
else:
    print("Student is not Found")