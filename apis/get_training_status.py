from flask_restplus import Namespace, fields, Resource
from flask import request

from ops.job_count_ops import JobCount

api = Namespace('get_training_status')

# Swagger params
api_parser = api.parser()
api_parser.add_argument('model_id', type=int, location='args')


@api.route('')
class GetTrainingStatus(Resource):

    @api.expect(api_parser, validate=True)
    @api.response(code=200, description="Training status")
    def get(self):
        data = request.args
        model_id = data["model_id"]
        jc_object = JobCount(model_id)
        training_status = jc_object.get_training_status()
        response = {"status": training_status}
        if training_status == JobCount.IN_TRAINING:
            response["progress"] = str(jc_object.get_progress_percent()) + "/100"
        return response, 200

