from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.place import Place
from ..models.user import User

places_bp = Blueprint('places', __name__)

# Create a place
@places_bp.route('/api/v1/places/', methods=['POST'])
@jwt_required()
def create_place():
    user_id = get_jwt_identity()
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    new_place = Place(
        name=name,
        description=description,
        owner_id=user_id
    )

    db.session.add(new_place)
    db.session.commit()

    return jsonify(new_place.to_dict()), 201

# Update a place
@places_bp.route('/api/v1/places/<int:place_id>/', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    user_id = get_jwt_identity()
    place = Place.query.get_or_404(place_id)

    if place.owner_id != user_id:
        return jsonify({'message': 'Unauthorized: You do not own this place.'}), 403

    data = request.get_json()
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)

    db.session.commit()
    return jsonify(place.to_dict()), 200

# Public end point - no JWT needed
@places_bp.route('/api/v1/places/', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places])
