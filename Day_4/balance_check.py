# Balance check in ATM machine

account_balance = 50000
system_pin = 1122

print("Welcome in ATM ")

enter_pin = int(input("Enter the correct pin : "))

if enter_pin == system_pin:

    print(f"Account Balance = {account_balance}")

else:

    print("Invalid pin")