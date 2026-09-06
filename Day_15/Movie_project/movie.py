movies = []

def add_movie(movie_id, name, genr, price):
    movie = {
        "id": movie_id,
        "name": name,
        "grnr": genr,
        "price": price,
    }

    movies.append(movie)

    print("Movie added sussesfully")

def display_movies():

    if not movies:
        print("No movie available.")
        return

    print("\n----------- MOVIE------------")

    for movie in movies:

        print(
            movie["id"],
            "|",
            movie["name"],
            "|",
            movie["genre"],
            "|",
            movie["price"],
            "|"
        )

def search_mpvie(name):

    for movie in movies:

        if movie["name"].lower() == name.lower():

            print("\nMovie Found!")
            print("ID:", movie["id"])
            print("Name:", movie["name"])
            print("Genre : ", movie["genre"])
            print("Ticket Price: ", movie["price"])

            return movie

    print("Movie not found.")
    return None