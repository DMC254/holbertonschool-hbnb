from flask_restx import Namespace, Resource, fields
from flask import request
from app.business.facade import HBNBFacade

api = Namespace('places', description='Place operations')
facade = HBNBFacade()

# Output model (excludes amenities/owner in nested form for simplicity)
place_model = api.model('Place', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float(required=True),
    'latitude': fields.Float,
    'longitude': fields.Float,
    'owner_id': fields.String(required=True),
    'amenity_ids': fields.List(fields.String),
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        data = request.json
        place = facade.create_place(data)
        return place, 201

    @api.marshal_list_with(place_model)
    def get(self):
        return facade.get_all_places()

@api.route('/<string:place_id>')
@api.param('place_id', 'The place identifier')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        place = facade.get_place_by_id(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place

    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        data = request.json
        place = facade.update_place(place_id, data)
        if not place:
            api.abort(404, "Place not found")
        return place
