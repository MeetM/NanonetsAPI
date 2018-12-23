from flask_restplus import Api

from .create_model import api as create_model_api

api = Api(
    title='Model training API',
    version='1.0',
    description='For Nanonets',
)

api.add_namespace(create_model_api)

