from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)
from ..extensions import db
from ..models.user import User
from ..facade.user_facade import UserFacade

users_bp = Blueprint('users', __name__)
facade = UserFacade()


# -------------------------
# USER REGISTRATION & LOGIN
# -------------------------

@users_bp.route('/api/v1/users/', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not password:
        return jsonify({'message': 'Email and password are required.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists.'}), 400

    new_user = User(
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    new_user.password = password  # triggers hashing
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@users_bp.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(
        identity=user.id,
        additional_claims={'is_admin': user.is_admin}
    )
    return jsonify({'access_token': access_token}), 200


# -------------------------
# AUTHENTICATED USER ACTIONS
# -------------------------

@users_bp.route('/api/v1/users/me', methods=['PUT'])
@jwt_required()
def update_current_user():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if 'email' in data or 'password' in data:
        return jsonify({'message': 'Cannot update email or password here.'}), 400

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@users_bp.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = facade.get_user(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


# -------------------------
# ADMIN-ONLY ROUTES
# -------------------------

@users_bp.route('/api/v1/admin-only-endpoint', methods=['POST'])
@jwt_required()
def admin_only_stuff():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({'message': 'Admins only!'}), 403

    return jsonify({'message': 'You did something as admin!'}), 200


@users_bp.route('/api/v1/admin/users/', methods=['POST'])
@jwt_required()
def admin_create_user():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({'message': 'Admins only!'}), 403

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists.'}), 409

    new_user = User(email=email, is_admin=is_admin)
    new_user.password = password
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@users_bp.route('/api/v1/admin/users/<int:user_id>/', methods=['PUT'])
@jwt_required()
def admin_update_user(user_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({'message': 'Admins only!'}), 403

    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if 'email' in data:
        existing = User.query.filter(User.email == data['email'], User.id != user_id).first()
        if existing:
            return jsonify({'message': 'Email already in use.'}), 409
        user.email = data['email']

    if 'password' in data:
        user.password = data['password']

    if 'is_admin' in data:
        user.is_admin = data['is_admin']

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)

    db.session.commit()
    return jsonify(user.to_dict()), 200
