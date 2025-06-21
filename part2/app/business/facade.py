from app.persistence.memory.repository import InMemoryRepository

class HBNBFacade:
    def __init__(self):
        self.repo = InMemoryRepository()

    def get_all_objects(self):
        return self.repo.all()
        
    def create_object(self, obj):
        return self.repo.save(obj)
