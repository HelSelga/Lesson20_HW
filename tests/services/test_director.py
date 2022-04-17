import pytest
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(21)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        new_dir = {"id": 24, "name": "Test Testov"}
        director = self.director_service.create(new_dir)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(23)

    def test_update(self):
        director = {"id": 22, "name": "Updated Name"}
        self.director_service.update(director)
