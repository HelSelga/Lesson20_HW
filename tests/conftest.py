from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    luxury = Movie(id=21, title="Title22", description="Description22", trailer="Trailer22", year=2022, rating=4.8, genre_id=4, director_id=6)
    singing_city = Movie(id=22, title="Title23", description="Description23", trailer="Trailer23", year=2023, rating=4.1, genre_id=7, director_id=12)

    movie_dao.get_one = MagicMock(return_value=luxury)
    movie_dao.get_all = MagicMock(return_value=[luxury, singing_city])
    movie_dao.create = MagicMock(return_value=Movie(id=22))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(id=19, name="TestGenre1")
    genre2 = Genre(id=20, name="TestGenre2")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2])
    genre_dao.create = MagicMock(return_value=Genre(id=20))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    cris = Director(id=21, name="Christina Robes")
    sam = Director(id=22, name="Samuel Jackson")
    dina = Director(id=23, name="Dina Stores")

    director_dao.get_one = MagicMock(return_value=cris)
    director_dao.get_all = MagicMock(return_value=[cris, sam, dina])
    director_dao.create = MagicMock(return_value=Director(id=23))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao
