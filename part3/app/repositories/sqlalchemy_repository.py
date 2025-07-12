from ..extensions import db

class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        return self.model.query.get(id)

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()

    def update(self):
        db.session.commit()

    def list_all(self):
        return self.model.query.all()
