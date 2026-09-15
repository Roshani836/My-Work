class Book:
    
    def __init__(self, book_name, auther, price ):
        self.book_name = book_name
        self.auther = auther
        self.price = price
        
    def display(self):
        print("Name:", self.book_name)
        print("Auther: ", self.auther)
        print("Price: ", self.price)
        
    def discount(self):
        if self.price > 500:
            discount = self.price *10/100
        else:
            discount = self.price*5/100
        
        Final_Price = self.price - discount
        
        print("Discount: ", discount)
        print("Final Price: ", Final_Price)
        
b1 = Book("Python Programming" , "ABC" , 600)

b1.display()
b1.discount()