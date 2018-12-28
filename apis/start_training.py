from flask_restplus import Namespace, fields, Resource
from flask import request
from ops.batch_ops import BatchOps
from ops.job_count_ops import JobCount

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
        jc = JobCount(model_id)
        if jc.get_training_status() != JobCount.TRAINING_NOT_STARTED:
            return {"error": "Training already started. This duplicate request is rejected."}, 409
        batch = BatchOps(model_id)
        for i in [0.01, 0.001, 0.0001]:
            for j in [1, 2]:
                for k in [1000, 2000, 4000]:
                    batch.schedule_training_job(i, j, k)
                    jc.incr_scheduled_job_count()
        batch.schedule_reducer_job()
        jc.incr_scheduled_job_count()
        return 201
