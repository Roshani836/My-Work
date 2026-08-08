prices  = {
    "Veg Burger":120,
    "Cheese Burger" :140,
    "Paneer Burger" :160,
    "Chicken Burger" : 200
}

item = "Chicken Burger"
quantity = 5

if item in prices:
    total_cost = prices[item] * quantity
    print(f"Cost for {quantity} X { item}: {total_cost}")
else:
    print("Item not found")