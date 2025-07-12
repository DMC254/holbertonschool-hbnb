from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt

from ..extensions import db
from ..models.amenity import Amenity

amenities_bp = Blueprint('amenities', __name__)

@amenities_bp.route('/api/v1/amenities/', methods=['POST'])
@jwt_required()
def create_amenity():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({'message': 'Admins only!'}), 403

    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name required'}), 400

    amenity = Amenity(name=name)
    db.session.add(amenity)
    db.session.commit()

    return jsonify(amenity.to_dict()), 201
