source = open("Create.txt" , "r")

data= source.read()

source.close()

destination = open("backup.txt", "w")

destination.write(data)

destination.close()

print("Your file copy Succesfully")