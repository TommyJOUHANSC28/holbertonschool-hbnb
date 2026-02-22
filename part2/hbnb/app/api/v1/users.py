"""
User API endpoints.
Handles CRUD operations for users.
DELETE is not implemented in Part 2.
"""

from flask_restx import Namespace, Resource, fields
from hbnb.app.services import facade

api = Namespace("users", description="User operations")



user_model = api.model("User", {
    "first_name": fields.String(required=True, description='First name of the user'),
    "last_name": fields.String(required=True, description='First name of the user'),
    "email": fields.String(required=True, description='First name of the user')
})


@api.route("/")
class UserList(Resource):
    """
    Handles user collection operations.
    """

    @api.expect(user_model, validate=True)
    @api.response(201, "User created")
    @api.response(400, "Invalid input")
    def post(self):
        """Create a new user"""
        try:
            user = facade.create_user(api.payload)
            return user.to_dict(), 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "Users retrieved")
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200


@api.route("/<string:user_id>")
class UserResource(Resource):
    """
    Handles single user operations.
    """

    @api.response(200, "User retrieved")
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200

    @api.expect(user_model, validate=True)
    @api.response(200, "User updated")
    @api.response(404, "User not found")
    def put(self, user_id):
        """Update user"""
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        user.update(api.payload)
        return user.to_dict(), 200
