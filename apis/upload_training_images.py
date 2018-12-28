from flask_restplus import Namespace, fields, Resource


api = Namespace('upload_training_images')

# Swagger params
_uti_request = api.model('Upload Training Images', {
    'model_id': fields.Integer(required=True, description='Model Id'),
    'src': fields.String(required=True, description='Source images folder path in s3 bucket'),
    'label': fields.String(required=True, description='Image labels')
})


@api.route('')
class UploadTrainingImages(Resource):

    @api.expect(_uti_request, validate=True)
    def post(self):
        # TODO 1. Copy images from src to destination s3 folder
        # TODO 2. Store training label in DB
        return 200
