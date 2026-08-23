import csv

Employee = [
    ["Id", "Room"],
    [11, "Room 201"],
    [12, "Room 105"],
    [13, "Room 304"]
]

with open("Employee.csv" , "w") as file:

    writer = csv.writer(file)

    writer.writerows(Employee)