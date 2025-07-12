from ..repositories.place_repository import PlaceRepository
from ..models.place import Place

class PlaceFacade:
    def __init__(self):
        self.repo = PlaceRepository()

    def get_place(self, id):
        return self.repo.get_by_id(id)

    def create_place(self, **kwargs):
        place = Place(**kwargs)
        return self.repo.add(place)

    def list_places(self):
        return self.repo.list_all()

    def update_place(self):
        self.repo.update()

    def delete_place(self, place):
        self.repo.delete(place)
