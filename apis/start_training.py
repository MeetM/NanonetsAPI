from flask_restplus import Namespace, fields, Resource
from flask import request
from models import db
from models.model_job import ModelJob
import boto3


api = Namespace('start_training')

# Swagger params
_st_request = api.model('Start Training Request', {
    'model_id': fields.Integer(required=True, description='Model Id')
})



@api.route('')
class StartTraining(Resource):

    @api.expect(_st_request, validate=True)
    def post(self):
        data = request.get_json()
        model_id = data["model_id"]

        job_ids =[]
        # create_job_queue(model_id, queue_name)
        for i in [0.01, 0.001, 0.001]:
            for j in [1, 2, 4]:
                for k in [1000, 2000, 4000]:
                    # id = create_job(job_name(model_id, i, j, k), i, j, k)
                    # job_ids.append(id)
                    pass
        # create_dependent_job(job_ids)
        return 201


def job_name(model_id, i, j, k):
    return str(model_id) + "_" + str(i) + "_" + str(j) + "_" + str(k)


# def create_job(job_name, i, j, k):
#     client = boto3.client('batch')
#     response = client.submit_job(
#         jobName=job_name,
#         jobQueue='nn-compute-environment',
#         jobDefinition='string',
#         parameters={
#             'string': 'string'
#         },
#         containerOverrides={
#             'vcpus': 123,
#             'memory': 123,
#             'command': [
#                 'string',
#             ],
#             'instanceType': 'string',
#             'environment': [
#                 {
#                     'name': 'string',
#                     'value': 'string'
#                 },
#             ]
#         },
#         nodeOverrides={
#             'nodePropertyOverrides': [
#                 {
#                     'targetNodes': 'string',
#                     'containerOverrides': {
#                         'vcpus': 123,
#                         'memory': 123,
#                         'command': [
#                             'string',
#                         ],
#                         'instanceType': 'string',
#                         'environment': [
#                             {
#                                 'name': 'string',
#                                 'value': 'string'
#                             },
#                         ]
#                     }
#                 },
#             ]
#         },
#         retryStrategy={
#             'attempts': 123
#         },
#         timeout={
#             'attemptDurationSeconds': 123
#         }
#     )