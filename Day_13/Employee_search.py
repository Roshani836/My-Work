import csv

search_id ="13"

with open("Employee.csv" , "r")as file:

    reader = csv.DictReader(file)
    for row in reader:
         if row["Id"].strip() == search_id:
                    print("Employee Found")
                    print("ID:" , row["Id"])
        
                    print("Room:" , row["Room"])