from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/v1/users/', methods=['POST'])
def register_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not all([email, password]):
        return jsonify({'message': 'Email and password are required.'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists.'}), 400
    
    new_user = User(
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    new_user.password = password  # Hash happens here

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201
