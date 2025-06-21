from flask_restx import Namespace, Resource, fields
from flask import request
from app.business.facade import HBNBFacade

api = Namespace('users', description='User operation')
facade = HBNBFacade()

user_model = api.model('User', {
    'id': fields.String(readonly=True),
    'email': fields.String(required=True),
    'name': fields.String(required=True),
})

create_user_model = api.model('CreateUser', {
    'email': fields.String(required=True),
    'name': fields.String(required=True),
    'password': fields.String(required=True),   # Not retuned in output
})
