import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(21)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        new_movie = {"id": 23, "title": "Title24", "description": "Description24",
                     "trailer": "Trailer24", "year": 2004, "rating": 4.2}
        movie = self.movie_service.create(new_movie)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(22)

    def test_update(self):
        movie = {"id": 21, "title": "TitleUpdated", "description": "DescriptionUpdated",
                 "trailer": "TrailerUpdated", "year": 2008, "rating": 4.6}
        self.movie_service.update(movie)
