from fastapi import FastAPI


app = FastAPI()
movies = [
    {"id": 1, "title": "Dune", "director": "Denis Villeneuve", "year": 2021},
    {"id": 2, "title": "Oppenheimer", "director": "Christopher Nolan", "year": 2023},
    {"id": 3, "title": "Parasite", "director": "Bong Joon-ho", "year": 2019},
    {"id": 4, "title": "Mad Max: Fury Road", "director": "George Miller", "year": 2015},
]


@app.get("/movies")
def get_movies():
    return movies
