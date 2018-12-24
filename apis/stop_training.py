from flask_restplus import Namespace, fields, Resource
from flask import request
from models import db
from models.model_job import ModelJob
import boto3


api = Namespace('stop_training')

# Swagger params
_stp_request = api.model('Stop Training Request', {
    'model_id': fields.Integer(required=True, description='Model Id')
})



@api.route('')
class StopTraining(Resource):

    @api.expect(_stp_request, validate=True)
    def delete(self):
        data = request.get_json()
        model_id = data["model_id"]

        # Get job queue
        # Stop the job queue if in process
        return 204