from flask_restplus import Namespace, fields, Resource
from flask import request
from ops.job_count_ops import JobCount

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
        job_status = JobCount(model_id)
        if job_status == JobCount.IN_TRAINING:
            return {"error": "Training in progress. Cannot delete"}, 409
        # TODO delete model training records if training completed
        return {}, 204
