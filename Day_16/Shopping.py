class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total(self):
        total = self.price * self.quantity
        print("Total: ", total)
        
    def display(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)
        
P1 = Product("Pen", 10 , 2)
P2 = Product("Notebook", 30 ,3)

P1.display()
P1.total()
print()

P2.display()
P2.total()
