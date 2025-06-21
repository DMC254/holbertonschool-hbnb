from flask_restx import Namespace, Resource, fields
from flask import request
from app.business.facade import HBNBFacade

api = Namespace('reviews', description='Review operations')
facade = HBNBFacade()

review_model = api.model('Review', {
    'id': fields.String(readonly=True),
    'text': fields.String(required=True),
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True),
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self):
        data = request.json
        review = facade.create_review(data)
        return review, 201

    @api.marshal_list_with(review_model)
    def get(self):
        return facade.get_all_reviews()

@api.route('/<string:review_id>')
@api.param('review_id', 'The review identifier')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        review = facade.get_review_by_id(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        data = request.json
        review = facade.update_review(review_id, data)
        if not review:
            api.abort(404, "Review not found")
        return review

    def delete(self, review_id):
        success = facade.delete_review(review_id)
        if not success:
            api.abort(404, "Review not found")
        return {'message': 'Review deleted successfully'}, 200
