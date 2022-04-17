import pytest
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(19)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_genre = {"id": 21, "name": "TestGenre3"}
        genre = self.genre_service.create(new_genre)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(21)

    def test_update(self):
        genre = {"id": 20, "name": "Updated Genre"}
        self.genre_service.update(genre)
