from ..extensions import db
from ..models.place import Place

class PlaceRepository:
    def __init__(self):
        self.model = Place

    def get_by_id(self, id):
        return self.model.query.get(id)

    def add(self, place):
        db.session.add(place)
        db.session.commit()
        return place

    def update(self):
        db.session.commit()

    def delete(self, place):
        db.session.delete(place)
        db.session.commit()

    def list_all(self):
        return self.model.query.all()
