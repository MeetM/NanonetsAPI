from flask_restplus import Namespace, fields, Resource
from flask import request
from models.model_job import ModelJob

api = Namespace('get_training_status')

# Swagger params
api_parser = api.parser()
api_parser.add_argument('model_id', type=int, location='args')


@api.route('')
class GetTrainingStatus(Resource):

    @api.expect(api_parser, validate=True)
    @api.response(code=200, description="Model deleted successfully")
    def get(self):
        data = request.args
        model_id = data["model_id"]
        job_queue = ModelJob.get_job_queue(model_id)
        status = "NotTrained"
        if job_queue is not None:
            pass
        return 204, {"status" : status}
