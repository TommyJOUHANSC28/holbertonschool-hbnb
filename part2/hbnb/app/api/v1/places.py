<<<<<<< HEAD
from flask_restx import Namespace, Resource

ns = Namespace('places', description='Places operations')

@ns.route('/')
class PlaceList(Resource):
    def get(self):
        return {"message": "List of places"}
=======
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

ns = Namespace('places', description='Place operations')

# --- Model for input validation & Swagger doc ---
place_model = ns.model('Place', {
    'title':       fields.String(required=True,  description='Title of the place'),
    'description': fields.String(required=False, description='Description of the place'),
    'price':       fields.Float (required=True,  description='Price per night'),
    'latitude':    fields.Float (required=True,  description='Latitude of the place'),
    'longitude':   fields.Float (required=True,  description='Longitude of the place'),
    'owner_id':    fields.String(required=True,  description='ID of the owner (user)'),
})


@ns.route('/')
class PlaceList(Resource):

    @ns.doc('list_places')
    def get(self):
        """Retrieve all places"""
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200

    @ns.doc('create_place')
    @ns.expect(place_model, validate=True)
    def post(self):
        """Create a new place"""
        data = ns.payload
        place = facade.create_place(data)
        return place.to_dict(), 201


@ns.route('/<string:place_id>')
@ns.param('place_id', 'The place unique identifier')
class PlaceResource(Resource):

    @ns.doc('get_place')
    def get(self, place_id):
        """Retrieve a place by ID"""
        place = facade.get_place(place_id)
        if not place:
            ns.abort(404, f"Place {place_id} not found")
        return place.to_dict(), 200

    @ns.doc('update_place')
    @ns.expect(place_model, validate=False)
    def put(self, place_id):
        """Update an existing place"""
        data = ns.payload
        place = facade.update_place(place_id, data)
        if not place:
            ns.abort(404, f"Place {place_id} not found")
        return place.to_dict(), 200

    @ns.doc('delete_place')
    def delete(self, place_id):
        """Delete a place by ID"""
        success = facade.delete_place(place_id)
        if not success:
            ns.abort(404, f"Place {place_id} not found")
        return {'message': 'Place deleted successfully'}, 200
>>>>>>> 2dc6a37 (add the file  code)
