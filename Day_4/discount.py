# Enter the amount 

print(" Welcome in mall ")

bill_amount = int(input("Enter the bill amount: "))

if bill_amount >=1000:

    print("Check discount coupon.")

    discount_coupon = (input("Enter the coupon information : "))

    if discount_coupon =="yes":

        print(" You are eligible for 10% Discount.")

    else:

        print("You are not eligible for 10% Discount ")

else:

    print("Do more shopping and get discount")