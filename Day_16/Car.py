class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model", self.model)
        print("Price: ", self.price)

car1 = Car("BMW" , "Series3", 62.70)
car2 = Car("BYD" , "Atto3", 24.99)
car3 = Car("Tesla " , "Model3", 55.00)

car1.display()
car2.display()
car3.display()