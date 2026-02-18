#!/usr/bin/python3
"""
Users API endpoints
Handles all HTTP requests related to users
"""
from flask_restx import Namespace, Resource, fields
from app.services import facade

ns = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = ns.model('User', {
    'first_name': fields.String(required=True,
                                description='First name of the user'),
    'last_name': fields.String(required=True,
                               description='Last name of the user'),
    'email': fields.String(required=True,
                           description='Email of the user')
})

# Define the response model for returning user data
user_response_model = ns.model('UserResponse', {
    'id': fields.String(required=True,
                        description='ID of the user'),
    'first_name': fields.String(required=True,
                                description='First name of the user'),
    'last_name': fields.String(required=True,
                               description='Last name of the user'),
    'email': fields.String(required=True,
                           description='Email of the user')
})


@ns.route('/')
class UserList(Resource):
    @ns.doc('Create a new user')
    @ns.marshal_with(user_response_model,
                      code=_http.HTTPStatus.CREATED,
                      description='User successfully created')
    @ns.expect(user_model, validate=False)
    @ns.response(201, 'User successfully created')
    @ns.response(400, 'Email already registered / Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = ns.payload
        try:
            compare_data_and_model(user_data, user_model)
            new_user = facade.create_user(user_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        return new_user, 201

    @ns.doc('Retrieve all users')
    @ns.marshal_list_with(user_response_model,
                          code=_http.HTTPStatus.OK,
                          description='List of users retrieved successfully')
    @ns.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get a list of registered users"""
        return facade.get_all_users(), 200


@ns.route('/<user_id>')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @ns.doc('Get user by ID')
    @ns.marshal_with(user_response_model,
                      code=_http.HTTPStatus.OK,
                      description='User details retrieved successfully')
    @ns.response(200, 'User details retrieved successfully')
    @ns.response(400, 'Invalid ID: not a UUID4 / Invalid input data')
    @ns.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        try:
            user = facade.get_user(user_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not user:
            ns.abort(404, error='User not found')
        return user, 200

    @ns.doc('Update a user')
    @ns.marshal_with(user_response_model,
                      code=_http.HTTPStatus.OK,
                      description='User updated successfully')
    @ns.expect(user_model, validate=False)
    @ns.response(200, 'User successfully updated')
    @ns.response(400, 'Invalid input data')
    @ns.response(404, 'User not found')
    def put(self, user_id):
        """Update an existing user's information"""
        user_data = ns.payload
        try:
            compare_data_and_model(user_data, user_model)
            updated_user = facade.update_user(user_id, user_data)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not updated_user:
            ns.abort(404, error='User not found')
        return updated_user, 200

    @ns.doc('Delete a user')
    @ns.response(204, 'User deleted successfully')
    @ns.response(400, 'Invalid ID: not a UUID4')
    @ns.response(404, 'User not found')
    def delete(self, user_id):
        """Delete a user"""
        try:
            success = facade.delete_user(user_id)
        except Exception as e:
            ns.abort(400, error=str(e))
        if not success:
            ns.abort(404, error='User not found')
        return '', 204
