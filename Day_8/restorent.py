order = ["Samosa","Juice","Sandwitch"]
items = [20,30,50]

grand_total=sum(items)

print("Welcome in resto")

for i in range(len(order)):
    print(f"{order[i]}: {items[i]}")

print("-------------------------")
print(f"Total amount : {grand_total}")