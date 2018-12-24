from flask_restplus import Api
from .delete_model import api as delete_model_api
from .create_model import api as create_model_api
from .get_training_status import api as get_training_status_api

api = Api(
    title='Model training API',
    version='1.0',
    description='For Nanonets',
)

api.add_namespace(create_model_api)
api.add_namespace(delete_model_api)
api.add_namespace(get_training_status_api)
