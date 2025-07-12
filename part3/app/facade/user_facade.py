from ..repositories.sqlalchemy_repository import SQLAlchemyRepository
from ..models.user import User

class UserFacade:
    def __init__(self):
        self.repo = SQLAlchemyRepository(User)

    def get_user(self, user_id):
        return self.repo.get(user_id)

    def create_user(self, **kwargs):
        user = User(**kwargs)
        return self.repo.add(user)

    def list_users(self):
        return self.repo.list_all()

    def delete_user(self, user):
        self.repo.delete(user)

    def update_user(self):
        self.repo.update()
