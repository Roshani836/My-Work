#project on reverse number

target_num =int(input("Enter the 3 digit number: "))

unit_digit = target_num % 10
dropped_factor = target_num // 10
tens_digit = dropped_factor %  10
hundread_digit = dropped_factor //10

reverse_value = (unit_digit * 100)+ (tens_digit * 10) + hundread_digit

print(f"Target Value : {target_num }" )
print(f"Reverse Value : {reverse_value}")