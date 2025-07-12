from ..extensions import db
from ..models.user import User

class UserRepository:
    def __init__(self):
        self.model = User

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_by_email(self, email):
        return self.model.query.filter_by(email=email).first()

    def add(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def update(self):
        db.session.commit()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()

    def list_all(self):
        return self.model.query.all()
