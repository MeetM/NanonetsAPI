from flask_restplus import Namespace, fields, Resource
from flask import request
from models.model_job import ModelJob

api = Namespace('delete_model')

# Swagger params
_delete_model_request = api.model('Delete Model', {
    'model_id': fields.Integer(required=True, description='Model Id')
})


@api.route('')
class DeleteModel(Resource):

    @api.expect(_delete_model_request, validate=True)
    @api.response(code=204, description="Model deleted successfully")
    def delete(self):
        data = request.get_json()
        model_id = data["model_id"]
        ModelJob.delete_model(model_id)
        return 204
