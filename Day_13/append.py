import csv

new_students = [ 104 , "Prerna" , "Computer" , "90"]

with open("marks.csv", "a" , newline="") as file:

    writer = csv.writer(file)

    writer.writerow(new_students)

