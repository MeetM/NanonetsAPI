from flask_restplus import Api
from .delete_model import api as delete_model_api
from .create_model import api as create_model_api
from .get_training_status import api as get_training_status_api
from .upload_training_images import api as upload_training_images_api
from .start_training import api as start_training_api
from .get_all_model_parameters import api as get_all_model_params_api
from .get_best_model_param import api as get_best_model_param_api


api = Api(
    title='Model training API',
    version='1.0',
    description='For Nanonets',
)

api.add_namespace(create_model_api)
api.add_namespace(delete_model_api)
api.add_namespace(get_training_status_api)
api.add_namespace(upload_training_images_api)
api.add_namespace(start_training_api)
api.add_namespace(get_all_model_params_api)
api.add_namespace(get_best_model_param_api)
