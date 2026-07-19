# Job eligibility 

print(" Welcome to the company")

written_exam = int(input("Enter the first round result: "))

if written_exam >=80 :

    print("You are eligible for next round.")

    coding_round = int(input( "Enter the Second round result: "))

    if coding_round >= 70:
        
        print("You are eligible for third round.")

        hr_interview = int(input("Enter the Third Round result: "))

        if hr_interview >=60:

            print(" Congratulation you are selected.")

        else:

            print("You are rejected.")

    else:

        print("You are not eligible.")

else:

    print("You have not pass.")