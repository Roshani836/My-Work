def calculate_bill(movie, seats):

    ticket_amount = movie["price"] * seats

    gst = ticket_amount * 18/100

    final_amount = ticket_amount + gst

    print("\n ----------Movie Bill-----------")

    print("Movie        : ",movie["name"])
    print("Genre        : ",movie["genre"])
    print("Ticket Price : ",movie["ticket price"])
    print("Seats        : ",seats)

    print("----------------------------")

    print("Ticket amount:", ticket_amount)
    print("Gst:", gst)
    print("Final Amount: ", final_amount)

    print(("===================="))
    return("final_amount")