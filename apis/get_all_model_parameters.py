from flask_restplus import Namespace, fields, Resource
from flask import request

from models.model_params import ModelParams
from ops.job_count_ops import JobCount

api = Namespace('get_all_model_params')

# Swagger params
api_parser = api.parser()
api_parser.add_argument('model_id', type=int, location='args')


@api.route('')
class GetAllModalParams(Resource):

    # TODO 1. proper response marshalling and validation
    # TODO 2. paginate
    @api.expect(api_parser, validate=True)
    def get(self):
        data = request.args
        model_id = data["model_id"]
        if JobCount(model_id).get_training_status() != JobCount.TRAINING_COMPLETE:
            return {"error": "Training not complete"}, 409
        params_json = {"params": ModelParams.get_params(int(model_id))}
        return params_json, 201
