from flask_restplus import Namespace, fields, Resource


api = Namespace('upload_training_images')

# Swagger params
_uti_request = api.model('Upload Training Images', {
    'src': fields.String(required=True, description='Source images folder path in s3 bucket'),
    'label': fields.String(required=True, description='Image labels')
})


@api.route('')
class UploadTrainingImages(Resource):

    @api.expect(_uti_request, validate=True)
    def post(self):
        # Transfer from src to destn S3 location
        return 200
