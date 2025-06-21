from app.persistence.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, email, name):
        super().__init__()
        self.email = email
        self.name = name
        self.places = []        # Place created by user
        self.reviews = []       # Reviews written by user

    def add_place(self, place):
        self.place.append(place)

    def add_review(self, review):
        self.review.append(review)
