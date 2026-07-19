# Blood donation eligibility check

print("Welcome in our blood donation camp")

age = int(input(" Enter the age of the persone: "))

if age >=18:

    weight = int(input("Enter the weight of the persone: "))

    if weight >=50:

        print("You are eligible for blood donation.")

    else:

        print("You are under weight. ")

else:

    print("You are not eligible for blood donation.")