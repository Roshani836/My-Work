cart ={
    "5 course mill": 500,
    "Chicken Burst": 600,
    "Big Big Pizza": 800,
    "Crespy Deals": 300,
    "Veg Pizza": 100
}

item= "Crespy Deals"
quantity = 4

if item in cart:
    total_cost = cart [item]* quantity
    print(f"cost for{quantity} X {item}: {total_cost}")
else:
    print("item not exist")

