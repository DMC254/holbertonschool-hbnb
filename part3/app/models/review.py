from ..extensions import db
from .base_model import BaseModel

class Review(BaseModel):
    __tablename__ = 'reviews'

    place_id = db.Column(db.Integer, nullable=False)  # FK later
    user_id = db.Column(db.Integer, nullable=False)   # FK later
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
        }
