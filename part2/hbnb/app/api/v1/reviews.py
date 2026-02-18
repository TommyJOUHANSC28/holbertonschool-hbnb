#!/usr/bin/python3
"""
Reviews API endpoints
Handles all HTTP requests related to reviews
"""
from flask_restx import Namespace, Resource, fields, _http
from app.services.facade import facade

ns = Namespace('reviews', description='Review operations')

# --- Input model: POST / PUT ---
review_model = ns.model('Review', {
    'text':     fields.String (required=True, description='Text of the review'),
    'rating':   fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id':  fields.String (required=True, description='ID of the user'),
    'place_id': fields.String (required=True, description='ID of the place')
})

# --- Output model: GET ---
review_response_model = ns.model('ReviewResponse', {
    'id':       fields.String (required=True, description='ID of the review'),
    'text':     fields.String (required=True, description='Text of the review'),
    'rating':   fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id':  fields.String(attribute=lambda r: r.user.id,
                              required=True, description='ID of the user'),
    'place_id': fields.String(attribute=lambda r: r.place.id,
                              required=True, description='ID of the place')
})


@ns.route('/')
class ReviewList(Resource):

    @ns.doc('list_reviews')
    @ns.marshal_list_with(review_response_model,
                          code=_http.HTTPStatus.OK,
                          description='List of reviews retrieved successfully')
    @ns.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        return facade.get_all_reviews(), 200

    @ns.doc('create_review')
    @ns.marshal_with(review_response_model,
                     code=_http.HTTPStatus.CREATED,
                     description='Review successfully created')
    @ns.expect(review_model, validate=True)
    @ns.response(201, 'Review successfully created')
    @ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        try:
            review = facade.create_review(ns.payload)
        except Exception as e:
            ns.abort(400, error=str(e))
        return review, 201


@ns.route('/<string:review_id>')
@ns.param('review_id', 'The review unique identifier')
class ReviewResource(Resource):

    @ns.doc('get_review')
    @ns.marshal_with(review_response_model,
                     code=_http.HTTPStatus.OK,
                     description='Review details retrieved successfully')
    @ns.response(200, 'Review details retrieved successfully')
    @ns.response(400, 'Invalid ID: not a UUID4')
    @ns.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        try:
            review = facade.get_review(review_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not review:
            ns.abort(404, error='Review not found')
        return review, 200

    @ns.doc('update_review')
    @ns.marshal_with(review_response_model,
                     code=_http.HTTPStatus.OK,
                     description='Review updated successfully')
    @ns.expect(review_model, validate=False)
    @ns.response(200, 'Review updated successfully')
    @ns.response(400, 'Invalid input data')
    @ns.response(404, 'Review not found')
    def put(self, review_id):
        """Update a review's information"""
        try:
            updated_review = facade.update_review(review_id, ns.payload)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not updated_review:
            ns.abort(404, error='Review not found')
        return updated_review, 200

    @ns.doc('delete_review')
    @ns.response(200, 'Review deleted successfully')
    @ns.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review by ID"""
        try:
            facade.delete_review(review_id)
        except Exception as e:
            ns.abort(404, error=str(e))
        return {'message': f'Review {review_id} deleted successfully'}, 200


@ns.route('/places/<string:place_id>/reviews')
@ns.param('place_id', 'The place unique identifier')
class PlaceReviewList(Resource):

    @ns.doc('get_reviews_by_place')
    @ns.marshal_list_with(review_response_model,
                          code=_http.HTTPStatus.OK,
                          description='List of reviews for the place retrieved successfully')
    @ns.response(200, 'List of reviews retrieved successfully')
    @ns.response(400, 'Invalid ID')
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            reviews = facade.get_reviews_by_place(place_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not reviews:
            ns.abort(404, error='Place not found')
        return reviews, 200
