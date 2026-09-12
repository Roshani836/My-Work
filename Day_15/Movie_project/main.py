import movie
import validation
import booking

def main():
    
    while true:
        
        print("\n==================================")
        print("                MOVIE BOOKING SYSTEM")
        PRINT("====================================")
        
        print("1. Add Movie")
        print("2. Display Movies")
        print("3. Search Movie")
        print("4. Book Tickets")
        print("5. Exit")
        
        choice = input("Enter your choice:")
        
        try:
            
            # Add Movie
            if choice == "1":
                
                movie_id = int(
                    input("Enter Movie ID: ")
                )
                
                name = input(
                    "Enter Movie name: "
                )
                
                genre = input(
                    "Enter Genre: "
                )
                
                price = float(
                    input("Enter Ticket Price: ")
                )
                
                val.validate_name(name)
                val.validate_price(price)
                
                movie.add_movie(
                    movie_id,
                    name,
                    genre,
                    price
                )
                
            # Display Movies
            elif choice == "2":
                
                movie.display_movies()
                
            #Search Movie
            elif choice == "3":
                
                name = input(
                    "Enter movie name to search: "
                )
                
                movie.search_movie(name)
                
            #Book Tickets
            elif choice == "4":
                
                name = input(
                    "Enter movie name: "
                )
                
                selected_movie = movie.search_movie(name)
                
                if selected_movie:
                    
                    seats = int(
                        input("Enter number of seats: ")
                    )
                    
                    val. validate_seats(seats)
                    
                    booking.calculate_bill(
                        selected_movie,
                        seats
                    )
                    
            #Exit
            elif choice == "5":
                
                print("Thank you for using Movie Booking System!")
                break
            
            else:
                
                print("Invalid choice!")
                
        except ValueError as e:
            
            print("Error:", e)
            
if __name__== "_main_":
    main()
