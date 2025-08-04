from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from ..extensions import db
from ..models.place import Place
from ..facade.place_facade import PlaceFacade

places_bp = Blueprint('places', __name__)
facade = PlaceFacade()


# -------------------------
# PUBLIC ROUTES
# -------------------------

@places_bp.route('/api/v1/places/', methods=['GET'])
def list_places():
    """Public - List all places"""
    places = facade.list_places()
    return jsonify([place.to_dict() for place in places]), 200


# -------------------------
# AUTHENTICATED USER ROUTES
# -------------------------

@places_bp.route('/api/v1/places/', methods=['POST'])
@jwt_required()
def create_place():
    """Authenticated - Create a new place"""
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


@places_bp.route('/api/v1/places/<int:place_id>/', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    """Authenticated - Update a place (owner or admin only)"""
    user_id = get_jwt_identity()
    claims = get_jwt()
    place = Place.query.get_or_404(place_id)

    if place.owner_id != user_id and not claims.get('is_admin'):
        return jsonify({'message': 'Unauthorized'}), 403

    data = request.get_json()
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)

    db.session.commit()
    return jsonify(place.to_dict()), 200
