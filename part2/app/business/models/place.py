from app.persistence.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, owner):
        super().__init__()
        self.name = name
        self.description = description
        self.owner = owner      # User object
        self.reviews = []       # List of Review objects
        self.amenities = []     # List of Amenity objects

        owner.add_place(self)
    
    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
