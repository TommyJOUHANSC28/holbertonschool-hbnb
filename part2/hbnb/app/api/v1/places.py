#!/usr/bin/python3
"""
Places API endpoints
Handles all HTTP requests related to places
"""
from flask_restx import Namespace, Resource, fields
from app.services import facade

ns = Namespace('places', description='Place operations')

# --- Nested model: owner (user) ---
user_model = ns.model('PlaceOwner', {
    'id':         fields.String(required=True, description='Owner ID'),
    'first_name': fields.String(required=True, description='First name of the owner'),
    'last_name':  fields.String(required=True, description='Last name of the owner'),
    'email':      fields.String(required=True, description='Email of the owner')
})

# --- Nested model: amenity ---
amenity_model = ns.model('PlaceAmenity', {
    'id':   fields.String(required=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Name of the amenity')
})

# --- Nested model: review ---
review_model = ns.model('PlaceReview', {
    'id':      fields.String(required=True, description='Review ID'),
    'text':    fields.String(required=True, description='Text of the review'),
    'rating':  fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(
        attribute=lambda review: review.user.id,
        required=True,
        description='ID of the user who left the review'
    )
})

# --- Input model: POST / PUT ---
place_model = ns.model('Place', {
    'title':       fields.String(required=True,  description='Title of the place'),
    'description': fields.String(required=False, description='Description of the place'),
    'price':       fields.Float (required=True,  description='Price per night'),
    'latitude':    fields.Float (required=True,  description='Latitude of the place'),
    'longitude':   fields.Float (required=True,  description='Longitude of the place'),
    'owner_id':    fields.String(required=True,  description='ID of the owner'),
    'amenities':   fields.List(fields.String,    required=True,
                               description="List of amenity IDs")
})

# --- Output model: GET (full detail with nested objects) ---
place_response_model = ns.model('PlaceResponse', {
    'id':          fields.String(required=True,  description='Unique identifier for the place'),
    'title':       fields.String(required=True,  description='Title of the place'),
    'description': fields.String(required=False, description='Description of the place'),
    'price':       fields.Float (required=True,  description='Price per night'),
    'latitude':    fields.Float (required=True,  description='Latitude of the place'),
    'longitude':   fields.Float (required=True,  description='Longitude of the place'),
    'owner':       fields.Nested(user_model,     required=True,  description='Owner of the place'),
    'amenities':   fields.List(fields.Nested(amenity_model), required=True,
                               description='List of amenities'),
    'reviews':     fields.List(fields.Nested(review_model),  required=True,
                               description='List of reviews')
})


@ns.route('/')
class PlaceList(Resource):

    @ns.doc('list_places')
    @ns.marshal_list_with(place_response_model,
                          code=_http.HTTPStatus.OK,
                          description='List of places retrieved successfully')
    @ns.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return places, 200

    @ns.doc('create_place')
    @ns.marshal_with(place_response_model,
                     code=_http.HTTPStatus.CREATED,
                     description='Place successfully created')
    @ns.expect(place_model, validate=True)
    @ns.response(201, 'Place successfully created')
    @ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = ns.payload
        try:
            place = facade.create_place(place_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        return place, 201


@ns.route('/<string:place_id>')
@ns.param('place_id', 'The place unique identifier')
class PlaceResource(Resource):

    @ns.doc('get_place')
    @ns.marshal_with(place_response_model,
                     code=_http.HTTPStatus.OK,
                     description='Place details retrieved successfully')
    @ns.response(200, 'Place details retrieved successfully')
    @ns.response(400, 'Invalid ID: not a UUID4')
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not place:
            ns.abort(404, error='Place not found')
        return place, 200

    @ns.doc('update_place')
    @ns.marshal_with(place_response_model,
                     code=_http.HTTPStatus.OK,
                     description='Place updated successfully')
    @ns.expect(place_model, validate=False)
    @ns.response(200, 'Place updated successfully')
    @ns.response(400, 'Invalid input data')
    @ns.response(404, 'Place not found')
    def put(self, place_id):
        """Update a place's information"""
        place_data = ns.payload
        try:
            updated_place = facade.update_place(place_id, place_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not updated_place:
            ns.abort(404, error='Place not found')
        return updated_place, 200


@ns.route('/<string:place_id>/reviews')
@ns.param('place_id', 'The place unique identifier')
class PlaceReviewsList(Resource):

    @ns.doc('get_place_reviews')
    @ns.marshal_list_with(review_model,
                          code=_http.HTTPStatus.OK,
                          description='List of reviews retrieved successfully')
    @ns.response(200, 'List of reviews retrieved successfully')
    @ns.response(400, 'Invalid ID')
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a place by its ID"""
        try:
            reviews = facade.get_reviews_by_place(place_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not reviews:
            ns.abort(404, error='Place not found')
        return reviews, 200
