from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Movie(BaseModel):
    title: str
    director: str
    year: int


movies = [
    {"id": 1, "title": "Dune", "director": "Denis Villeneuve", "year": 2021},
    {"id": 2, "title": "Oppenheimer", "director": "Christopher Nolan", "year": 2023},
    {"id": 3, "title": "Parasite", "director": "Bong Joon-ho", "year": 2019},
    {"id": 4, "title": "Mad Max: Fury Road", "director": "George Miller", "year": 2015},
]


def find_movie(movie_id: int):
    for m in movies:
        if m["id"] == movie_id:
            return m
    raise HTTPException(status_code=404, detail="Movie not found")


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
    return find_movie(movie_id)


@app.post("/movies", status_code=201)
def add_movie(movie: Movie):
    next_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": next_id, **movie.model_dump()}
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update(movie.model_dump())
    return existing


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
