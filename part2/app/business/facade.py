from app.business.models.review import Review

class HBNBFacade:
    # ... existing methods ...

    def create_review(self, data):
        required = ['text', 'user_id', 'place_id']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing field: {field}")

        user = self.repo.get(data['user_id'])
        if not user or user.get('type') != 'User':
            raise ValueError("Invalid user ID")

        place = self.repo.get(data['place_id'])
        if not place or place.get('type') != 'Place':
            raise ValueError("Invalid place ID")

        review = Review(
            text=data['text'],
            user=user,
            place=place
        )
        return self.repo.save(review)

    def get_all_reviews(self):
        return [r for r in self.repo.all() if r.get('type') == 'Review']

    def get_review_by_id(self, review_id):
        review = self.repo.get(review_id)
        if review and review.get('type') == 'Review':
            return review
        return None

    def update_review(self, review_id, data):
        review = self.repo.get(review_id)
        if not review or review.get('type') != 'Review':
            return None

        if 'text' in data:
            review['text'] = data['text']

        self.repo.update(review_id, review)
        return review

    def delete_review(self, review_id):
        review = self.repo.get(review_id)
        if not review or review.get('type') != 'Review':
            return False

        self.repo.delete(review_id)
        # Also remove review from place and user objects if you track those links
        if review.place:
            try:
                review.place.reviews.remove(review)
            except ValueError:
                pass
        if review.user:
            try:
                review.user.reviews.remove(review)
            except ValueError:
                pass

        return True
