import shopping

product = input("Enter the product name: ")
price  = int(input("Enter the price: "))
quantity = int(input("Enter the quantity:"))

print(shopping.product_bill(price,quantity))