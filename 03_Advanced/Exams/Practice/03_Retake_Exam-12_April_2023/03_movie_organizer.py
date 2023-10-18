def movie_organizer(*args):
    movies = {}
    result = ""

    for el in args:
        if el[1] not in movies:
            movies[el[1]] = []

        movies[el[1]].append(el[0])

    movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0],))

    for gender, collected in movies:
        collected.sort()
        result += f"{gender} - {len(collected)}\n" + "\n".join(f"* {x}" for x in collected) + "\n"

    return result[:-1]


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
