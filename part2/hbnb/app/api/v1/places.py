from flask_restx import Namespace, Resource

ns = Namespace('places', description='Places operations')

@ns.route('/')
class PlaceList(Resource):
    def get(self):
        return {"message": "List of places"}