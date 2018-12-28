import boto3
import os


class BatchOps:

    def __init__(self, model_id):
        self.model_id = model_id
        self.training_job_ids = []

    def schedule_training_job(self, i, j, k):
        client = boto3.client('batch')
        job_name = str(self.model_id) + "_" + str(int(i)) + "_" + str(int(j)) + "_" + str(int(k))
        response = client.submit_job(
            jobName=job_name,
            jobQueue=os.environ["JOB_Q"],
            jobDefinition=os.environ['TRAINING_JOB_DEF_ARN'],
            containerOverrides={
                'environment': [
                    {
                        'name': 'MODEL_ID',
                        'value': str(self.model_id)
                    },
                    {
                        'name': 'MODEL_I',
                        'value': str(i)
                    },
                    {
                        'name': 'MODEL_J',
                        'value': str(j)
                    },
                    {
                        'name': 'MODEL_K',
                        'value': str(k)
                    },
                ]
            }
        )
        self.training_job_ids.append({"jobId": response["jobId"]})

    def schedule_reducer_job(self):
        client = boto3.client('batch')
        job_name = str(self.model_id) + "_REDUCER_"
        client.submit_job(
            jobName=job_name,
            jobQueue=os.environ["JOB_Q"],
            jobDefinition=os.environ["REDUCER_JOB_DEF_ARN"],
            dependsOn=self.training_job_ids,
            containerOverrides={
                'environment': [
                    {
                        'name': 'MODEL_ID',
                        'value': str(self.model_id)
                    }
                ]
            }
        )
