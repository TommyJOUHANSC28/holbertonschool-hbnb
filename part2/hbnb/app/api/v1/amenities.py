#!/usr/bin/python3
"""
Amenities API endpoints
Handles all HTTP requests related to amenities
"""
from http import HTTPStatus
from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from .app.services import facade

ns = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = ns.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

# Define the response model for returning amenity data
amenity_response_model = ns.model('AmenityResponse', {
    'id': fields.String(
        required=True,
        description='Unique identifier for the amenity'),
    'name': fields.String(required=True,
                          description='Name of the amenity')
})


@ns.route('/')
class AmenityList(Resource):
    @ns.doc('Create a new amenity')
    @ns.marshal_with(amenity_response_model,
                      code=_http.HTTPStatus.CREATED,
                      description='Amenity successfully created')
    @ns.expect(amenity_model, validate=False)
    @ns.response(201, 'Amenity successfully created',
                  amenity_response_model)
    @ns.response(400, 'Name already assigned / Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = ns.payload
        try:
            compare_data_and_model(amenity_data, amenity_model)
            new_amenity = facade.create_amenity(amenity_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        return new_amenity, 201

    @ns.doc('Retrieve all amenities')
    @ns.marshal_list_with(
        amenity_response_model,
        code=_http.HTTPStatus.OK,
        description='List of amenities retrieved successfully')
    @ns.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        return facade.get_all_amenities(), 200


@ns.route('/<amenity_id>')
@ns.param('amenity_id', 'The amenity identifier')
class AmenityResource(Resource):
    @ns.doc('Get amenity by ID')
    @ns.marshal_with(
        amenity_response_model,
        code=_http.HTTPStatus.OK,
        description='Amenity details retrieved successfully')
    @ns.response(200, 'Amenity details retrieved successfully')
    @ns.response(400, 'Invalid ID: not a UUID4 / Invalid input data')
    @ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        try:
            amenity = facade.get_amenity(amenity_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not amenity:
            ns.abort(404, error='Amenity not found')
        return amenity, 200

    @ns.doc('Update an amenity')
    @ns.marshal_with(amenity_response_model,
                      code=_http.HTTPStatus.OK,
                      description='Amenity updated successfully')
    @ns.expect(amenity_model, validate=False)
    @ns.response(200, 'Amenity updated successfully')
    @ns.response(400, 'Invalid input data')
    @ns.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = ns.payload
        try:
            compare_data_and_model(amenity_data, amenity_model)
            updated_amenity = facade.update_amenity(amenity_id,
                                                    amenity_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not updated_amenity:
            ns.abort(404, error='Amenity not found')
        return updated_amenity, 200

    @ns.doc('Delete an amenity')
    @ns.response(204, 'Amenity deleted successfully')
    @ns.response(400, 'Invalid ID: not a UUID4')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an amenity"""
        try:
            success = facade.delete_amenity(amenity_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not success:
            ns.abort(404, error='Amenity not found')
        return '', 204
