from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__
    
    def update_timestamp(self):
        self.updated_at = datetime.now()
