class Mobile:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)

mobile1 = Mobile("Samsung", "M36" ,23290)
mobile2 = Mobile("POCO", "M7 Pro" , 14999)
mobile3 = Mobile("Vivo", "T4x", 14999)

mobile1.display()
mobile2.display()
mobile3.display()

        