from flask_restplus import Namespace, fields, Resource
from flask import request

from ops.best_params import fetch_best_params
from ops.job_count_ops import JobCount

api = Namespace('get_best_model_params')

# Swagger params
api_parser = api.parser()
api_parser.add_argument('model_id', type=int, location='args')

_get_best_params_response = api.model('Best Params Response', {
    'i': fields.Float(required=True, description='I'),
    'j': fields.Float(required=True, description='J'),
    'k': fields.Float(required=True, description='K'),
    'acc': fields.Float(required=True, description='Accuracy')
})


@api.route('')
class GetBestModelParam(Resource):

    @api.expect(api_parser, validate=True)
    @api.response(code=201, model=_get_best_params_response, description='Best Params Response')
    def get(self):
        data = request.args
        model_id = data["model_id"]
        if JobCount(model_id).get_training_status() != JobCount.TRAINING_COMPLETE:
            return {"error": "Training not complete"}, 409
        best_params = fetch_best_params(model_id)
        return best_params, 200
