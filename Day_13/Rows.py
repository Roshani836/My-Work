import csv

students = [
    ["Id" , "name" , "Branch" , "marks"],
    [101, "Rahul" , "Computer", 80],
    [102, "Priya" , "IT", 70],
    [103, "Mahesh" , "Mech", 90]
]

with open("marks.csv", "w", newline="") as  file:
    writer = csv.writer(file)

    writer.writerows(students)