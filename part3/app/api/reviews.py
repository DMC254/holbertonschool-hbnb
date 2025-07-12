from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.review import Review
from ..models.user import User

reviews_bp = Blueprint('reviews', __name__)

# Create new review
@reviews_bp.route('/api/v1/places/<int:place_id>/reviews/', methods=['POST'])
@jwt_required()
def create_review(place_id):
    user_id = get_jwt_identity()
    place = Place.query.get_or_404(place_id)

    # prevent reviewing own place
    if place.owner_id == user_id:
        return jsonify({'message': 'You cannot review your own place.'}), 403
    
    # Prevent duplicate review
    existing_review = Review.query.filter_by(place_id=place_id, user_id=user_id).first()
    if existing_review:
        return jsonify({'message': 'You have already reviewd this place.'}), 409
    
    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')

    if not content or not rating:
        return jsonify({'message': 'Content and rating are required.'}), 400
    
    review = Review(
        content=content,
        rating=rating,
        place_id=place_id,
        user_id=user_id
    )

    db.session.add(review)
    db.session.commit()

    return jsonify(review.to_dict()), 201
