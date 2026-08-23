import csv

with open("student.csv", "w" , newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID" , "Name" , "Branch" , "Marks"])
    writer.writerow([101, "Rahul" , "Computer", 80])
    writer.writerow([102, "Priya" , "IT", 90])
    writer.writerow([103, "Amit" , "Mechanical", 70])

print("CSV file created successfully!")