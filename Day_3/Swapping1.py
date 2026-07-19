# Swaping number without using third variable

a = int(input(" a = "))
b = int(input(" a = "))

print(f"\nBefore Swaping: A ={a} , B ={b}")

a=a+b
b=a-b
a=a-b

print(f"\nAfter Swapping: A = {a} , B = {b}")