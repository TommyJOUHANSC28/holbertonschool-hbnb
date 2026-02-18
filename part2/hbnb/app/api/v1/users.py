from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

ns = Namespace('users', description='User operations')

# --- Model for input validation & Swagger doc ---
user_model = ns.model('User', {
    'first_name': fields.String(required=True,  description='First name of the user'),
    'last_name':  fields.String(required=True,  description='Last name of the user'),
    'email':      fields.String(required=True,  description='Email address of the user'),
})


@ns.route('/')
class UserList(Resource):

    @ns.doc('list_users')
    def get(self):
        """Retrieve all users"""
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200

    @ns.doc('create_user')
    @ns.expect(user_model, validate=True)
    def post(self):
        """Create a new user"""
        data = ns.payload
        user = facade.create_user(data)
        return user.to_dict(), 201


@ns.route('/<string:user_id>')
@ns.param('user_id', 'The user unique identifier')
class UserResource(Resource):

    @ns.doc('get_user')
    def get(self, user_id):
        """Retrieve a user by ID"""
        user = facade.get_user(user_id)
        if not user:
            ns.abort(404, f"User {user_id} not found")
        return user.to_dict(), 200

    @ns.doc('update_user')
    @ns.expect(user_model, validate=False)
    def put(self, user_id):
        """Update an existing user"""
        data = ns.payload
        user = facade.update_user(user_id, data)
        if not user:
            ns.abort(404, f"User {user_id} not found")
        return user.to_dict(), 200

    @ns.doc('delete_user')
    def delete(self, user_id):
        """Delete a user by ID"""
        success = facade.delete_user(user_id)
        if not success:
            ns.abort(404, f"User {user_id} not found")
        return {'message': 'User deleted successfully'}, 200
