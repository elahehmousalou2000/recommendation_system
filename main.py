movies = {
    "Inception": ["Interstellar", "Tenet"],
    "Interstellar": ["Inception", "Gravity"],
    "Titanic": ["Avatar"],
}

movie = input("Movie: ").strip()

recommendations = movies.get(movie)

if recommendations:
    print("Recommended:")
    for item in recommendations:
        print("-", item)
else:
    print("Movie not found.")
