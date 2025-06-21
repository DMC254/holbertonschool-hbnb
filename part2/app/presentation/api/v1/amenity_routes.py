from flask_restx import Namespace, Resource, fields
from flask import request
from app.business.facade import HBNBFacade

api = Namespace('amenities', description='Amenity operations')
facade = HBNBFacade()

# Amenity model schema
amenity_model = api.model('Amenity', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.json
        amenity = facade.create_amenity(data['name'])
        return amenity, 201

    @api.marshal_list_with(amenity_model)
    def get(self):
        """Get all amenities"""
        return facade.get_all_amenities()

@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Get amenity by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update amenity name"""
        data = request.json
        amenity = facade.update_amenity(amenity_id, data)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity
