from ..extensions import db
from .base_model import BaseModel

class Place(BaseModel):
    __tablename__ = 'places'

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)  # FK in future

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'price': self.price,
            'owner_id': self.owner_id,
        }
