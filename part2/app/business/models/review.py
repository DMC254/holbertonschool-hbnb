from app.persistence.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user, place, text):
        super().__init__()
        self.user = user        # User object
        self. place - place     # Place object
        self.text = text

        user.add_review(self)
        place.add_review(self)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user.id if self.user else None,
            'place_id': self.place.id if self.place else None,
            'type': self.type,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
