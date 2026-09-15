class Movie:
    
    def __init__(self, movie_name, ticket_price, seats):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.seats = seats
        
    def calculate_bill(self):
        total = self.ticket_price * self.seats
        print("Total: ", total)
    
    def display(self):
        print("Movie Name: ",self.movie_name)
        print("Ticket price: ", self.ticket_price)
        print("Seats: ", self.seats)
        
movie1 = Movie("Avengers", 200, 3)
movie1.display()
movie1.calculate_bill()




