from app.persistence.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, owner):
        super().__init__()
        self.name = name
        self.description = description
        self.owner = owner              # User object
        self.amenities = []            # List of Amenity objects
        self.reviews = []              # List of Review objects
        self.type = "Place"

        # Link this place to the owner
        owner.add_place(self)

    def add_amenity(self, amenity):
        """Attach an amenity object to this place."""
        self.amenities.append(amenity)

    def add_review(self, review):
        """Attach a review object to this place."""
        self.reviews.append(review)

    def to_dict(self):
        """Serialize Place object to a flat dictionary (no nested objects)."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner.id if self.owner else None,
            'amenity_ids': [amenity.id for amenity in self.amenities],
            'review_ids': [review.id for review in self.reviews],
            'type': self.type,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
