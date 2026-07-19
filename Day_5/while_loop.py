CORRECT_PIN = "1234"
security_pin = ""

while security_pin != CORRECT_PIN:

    security_pin = input("Enter the 4 digit pin: ")

    if security_pin != CORRECT_PIN:

        print(f"Access Denied. Enter Correct pin .")

print(" Access Granted! Enter the amount")