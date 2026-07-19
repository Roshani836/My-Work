acount_balance = 100000
system_pin = 1122

print(" Welcome TO ATM")

enter_pin = int(input("Enter the Valid pin: "))

if enter_pin == system_pin:

    print("Pin verified successfully. ")

    deposite_amount = float(input("Enter the  deposite amount: "))

    deposite_amount+=acount_balance

   
    print(f" Account Balance: {deposite_amount}")

else:

    print(" You enter invalid pin.")