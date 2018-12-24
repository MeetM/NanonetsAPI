from flask_restplus import Namespace, fields, Resource
from flask import request
from models import db
from models.model_job import ModelJob
import boto3

api = Namespace('get_all_model_params')

# Swagger params
api_parser = api.parser()
api_parser.add_argument('model_id', type=int, location='args')


@api.route('')
class GetBestModalParams(Resource):

    @api.expect(api_parser, validate=True)
    def get(self):
        data = request.get_json()
        model_id = data["model_id"]

        # query db to get all model params
        # create and return a json object with the model params
        return 200, {"res" : [{"i" : "i1", "j" : "j1", "k" : "k1"},
                              {"i": "i2", "j": "j2", "k": "k2"}]}
