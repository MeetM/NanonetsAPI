from flask_restplus import Namespace, fields, Resource
from flask import request
from models import db
from models.model_job import ModelJob

api = Namespace('create_model')

# Swagger params
_create_model_request = api.model('Create Model', {
    'name': fields.String(required=True, description='Model Name'),
    'desc': fields.String(required=False, description='Model Description')
})

_create_model_response = api.model('Create Model Response', {
    'model_id': fields.Integer(required=True, description='Model Id')
})


@api.route('')
class CreateModel(Resource):

    @api.expect(_create_model_request, validate=True)
    @api.response(code=201, model=_create_model_response, description="Model created successfully")
    def post(self):
        data = request.get_json()
        name = data["name"]
        desc = data["desc"]
        model = ModelJob(name=name, desc=desc)
        db.session.add(model)
        db.session.commit()
        model_id = model.get_model_id()
        return {'model_id': model_id}, 201
