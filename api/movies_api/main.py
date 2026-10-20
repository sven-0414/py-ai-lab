from fastapi import FastAPI


app = FastAPI()
movies = [
    {"id": 1, "title": "Dune", "director": "Denis Villeneuve", "year": 2021},
    {"id": 2, "title": "Oppenheimer", "director": "Christopher Nolan", "year": 2023},
    {"id": 3, "title": "Parasite", "director": "Bong Joon-ho", "year": 2019},
    {"id": 4, "title": "Mad Max: Fury Road", "director": "George Miller", "year": 2015},
]


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    result = movies
    if director is not None:
        result = [m for m in result if director.lower() in m["director"].lower()]
    if year is not None:
        result = [m for m in result if m["year"] == year]
    return result


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for m in movies:
        if m["id"] == movie_id:
            return m
