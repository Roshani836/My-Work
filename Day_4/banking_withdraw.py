#The project om ATM bamking withdraw

account_balance = 100000
system_pin = 4255

print("Welcome in the ATM")
enter_pin = int(input(" Ente the four digit pin (eg: 1234) :  "))

if enter_pin == system_pin:

    print("Pin verified successfully.")

    withdraw_amount = float(input("Enter the amount: "))

    if withdraw_amount <= account_balance:
        account_balance -= withdraw_amount 

        print(f" Amount Withdraw Successfylly : {withdraw_amount}")
        print(f"Check Account Balance: {account_balance}")

    else:

        print(" Insufficient amount")

else:

    print("Wrong pin Enter ")