from flask import Flask
from flask_restx import Api
from app.api.v1.users import ns as users_ns
from app.api.v1.places import ns as places_ns
from app.api.v1.reviews import ns as reviews_ns
from app.api.v1.amenities import ns as amenities_ns

def create_app(config_name='default'):
    app = Flask(__name__)

    # Load configuration
    from config import config
    app.config.from_object(config[config_name])

    # Initialize REST API with Flask-RESTX
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='REST API for the HBnB (Airbnb) clone',
        doc='/api/v1/'
    )

    # Register namespaces (RESTX blueprints)
    api.add_namespace(users_ns,     path='/api/v1/users')
    api.add_namespace(places_ns,    path='/api/v1/places')
    api.add_namespace(reviews_ns,   path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
