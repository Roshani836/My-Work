cart = []

while True:

    print("\n===== SHOPPPING CART ======")
    print("1, Add product")
    print("2, View Cart")
    print("3, Total Bill")
    print("4, Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:

            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            if price <=0:
                raise ValueError("Price must be grater than 0")

            if quantity <= 0:
                raise ValueError("Quantity must be grater than 0")

            item = {
                "name" : name,
                "price" : price,
                "quantity" : quantity
            }

            cart.append(item)

            print("product added to cart: ")

        elif choice == 2:

            if len(cart) == 0:
                print("Cart is empty")

            else:
                print("\n ===== Your Cart ======")

                for item in cart:
                    total = item["price"] * item["quantity"]

                    print("Product :", item["name"])
                    print("Price :", item["price"])
                    print("Quantity :", item["quantity"])
                    print("Total :", total)
                    print("----------------")

        elif choice == 3:

            grand_total = 0

            for item in cart:
                total = item["price"]* item["quantity"]
                grand_total += total

            print("Grand Total =", grand_total)

        elif choice == 4:

            print("Thank you for shopping")
            break

        else:
            print("Please select 1 to 4")

    except ValueError as e:
        print("Error :" , e)
    finally:
        print("Operation Completed")


