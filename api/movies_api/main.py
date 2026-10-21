import json
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Header
from fastapi import FastAPI
from pydantic import BaseModel


MOVIES_FILE = Path("movies.json")


def load_movies():
    if MOVIES_FILE.exists():
        with open(MOVIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {"id": 1, "title": "Dune", "director": "Denis Villeneuve", "year": 2021},
        {
            "id": 2,
            "title": "Oppenheimer",
            "director": "Christopher Nolan",
            "year": 2023,
        },
        {"id": 3, "title": "Parasite", "director": "Bong Joon-ho", "year": 2019},
        {
            "id": 4,
            "title": "Mad Max: Fury Road",
            "director": "George Miller",
            "year": 2015,
        },
    ]


load_dotenv()
movies = load_movies()
API_KEY = os.getenv("SUPER_SECRET_KEY")
app = FastAPI()


class Movie(BaseModel):
    title: str
    director: str
    year: int


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


def check_key(x_api_key: str | None = Header(default=None)):
    if API_KEY is None:
        raise HTTPException(status_code=500, detail="Server misconfigured")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


def find_movie(movie_id: int):
    for m in movies:
        if m["id"] == movie_id:
            return m
    raise HTTPException(status_code=404, detail="Movie not found")


def save_movies():
    with open(MOVIES_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)


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


@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):
    next_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": next_id, **movie.model_dump()}
    movies.append(new_movie)
    save_movies()
    return new_movie


@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update(movie.model_dump())
    save_movies()
    return existing


@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
    save_movies()


@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_id: int, changes: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(changes.model_dump(exclude_unset=True))
    save_movies()
    return movie


# Använd PUT när klienten skickar hela det uppdaterade objektet och vill ersätta.
# Använd PATCH när klienten bara skickar de fält som ska ändras.
