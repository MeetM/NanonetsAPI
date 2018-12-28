import os
import redis


class JobCount:

    IN_TRAINING = "InTraining"
    TRAINING_COMPLETE = "TrainingComplete"
    TRAINING_NOT_STARTED = "TrainingNotStarted"

    def __init__(self, model_id):
        redis_url = os.environ['REDIS_URL']
        self.db = redis.StrictRedis(host=redis_url, port=6379, db=0)
        self.model_id = model_id

    def get_scheduled_jobs_count(self):
        job_count = self.db.get(JobCount._scheduled_count_key(self.model_id))
        if job_count is not None:
            return int(job_count)
        return 0

    def get_completed_jobs_count(self):
        job_count = self.db.get(JobCount._completed_count_key(self.model_id))
        if job_count is not None:
            return int(job_count)
        return 0

    def incr_scheduled_job_count(self):
        self.db.incr(JobCount._scheduled_count_key(self.model_id), amount=1)

    def get_training_status(self):
        scheduled_jc = self.get_scheduled_jobs_count()
        completed_jc = self.get_completed_jobs_count()
        assert scheduled_jc >= completed_jc
        # FIXME - currently, this will return TRAINING_NOT_STARTED for non-existent models
        response = JobCount.TRAINING_NOT_STARTED
        if scheduled_jc != 0 and scheduled_jc == completed_jc:
            response = JobCount.TRAINING_COMPLETE
        elif completed_jc != 0 and scheduled_jc > completed_jc:
            response = JobCount.IN_TRAINING
        return response

    def get_progress_percent(self):
        scheduled_jc = self.get_scheduled_jobs_count()
        completed_jc = self.get_completed_jobs_count()
        assert scheduled_jc >= completed_jc
        return completed_jc * 100/scheduled_jc

    @staticmethod
    def _scheduled_count_key(model_id):
        return "JOB_SCHEDULED_COUNT_" + str(model_id)

    @staticmethod
    def _completed_count_key(model_id):
        return "JOB_COMPLETED_COUNT_" + str(model_id)
