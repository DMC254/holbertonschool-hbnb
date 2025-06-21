from flask_restx import Namespace, Resource, fields
from flask import request
from app.business.facade import HBNBFacade

api = Namespace('users', description='User operations')
facade = HBNBFacade()

user_model = api.model('User', {
    'id': fields.String(readonly=True),
    'email': fields.String(required=True),
    'name': fields.String(required=True),
})

create_user_model = api.model('CreateUser', {
    'email': fields.String(required=True),
    'name': fields.String(required=True),
    'password': fields.String(required=True),
})

@api.route('/')
class UserList(Resource):
    @api.expect(create_user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        data = request.json
        user = facade.create_user(data['email'], data['name'], data['password'])
        return user, 201

    @api.marshal_list_with(user_model)
    def get(self):
        return facade.get_all_users()

@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        user = facade.get_user_by_id(user_id)
        if not user:
            api.abort(404, "User not found")
        return user

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        data = request.json
        user = facade.update_user(user_id, data)
        if not user:
            api.abort(404, "User not found")
        return user
