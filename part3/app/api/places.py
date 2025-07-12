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

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from ..extensions import db
from ..models.place import Place

places_bp = Blueprint('places', __name__)

@places_bp.route('/api/v1/places/<int:place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    user_id = get_jwt_identity()
    claims = get_jwt()

    place = Place.query.get_or_404(place_id)

    # Check if the user owns the place OR is admin
    if place.owner_id != user_id and not claims.get('is_admin'):
        return jsonify({'message': 'Unauthorized'}), 403

    data = request.get_json()
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)

    db.session.commit()
    return jsonify(place.to_dict()), 200

from flask import Blueprint, request, jsonify
from ..facade.place_facade import PlaceFacade

places_bp = Blueprint('places', __name__)
facade = PlaceFacade()

@places_bp.route('/api/v1/places/', methods=['POST'])
def create_place():
    data = request.get_json()
    place = facade.create_place(**data)
    return jsonify(place.to_dict()), 201

@places_bp.route('/api/v1/places/', methods=['GET'])
def list_places():
    places = facade.list_places()
    return jsonify([p.to_dict() for p in places]), 200
