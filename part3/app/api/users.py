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

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models.user import User
from ..extensions import db

users_bp = Blueprint('users', __name__)

# Register user already exists here

@users_bp.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({'message': 'Email and password required'}),400
    
    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # Include custom claims if needed
    access_token = create_access_token(identity=user.id, additional_claims={'is_admin': user.is_admin})

    return jsonify({'access_token': access_token}), 200

@users_bp.route('.api/v1/users/me', methods=['PUT'])
@jwt_required()
def update_current_user():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    data = request.get_json()

    # Do NOT allow email or password update here
    if 'email' in data or 'password' in data:
        return jsonify({'message': 'You cannot update email or password here.'}), 400
    
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)

    db.session.commit()
    return jsonify(user.to_dict()), 200
