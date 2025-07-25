import uuid

class InMemoryRepository:
    def __init__(self):
        self.storage = {}

    def save(self, obj):
        obj_id = str(uuid.uuid4())
        obj['id'] = obj_id
        self.storage[obj_id] = obj
        return obj
    
    def get(self, obj_id):
        return self.storage.get(obj_id)
    
    def all(self):
        return list(self.storage.values())
    
    def delete(self, obj_id):
        return self.storage.pop(obj_id, None)
