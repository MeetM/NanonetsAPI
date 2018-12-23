from models import db


class ModelJob(db.Model):

    __tablename__ = 'modeljob'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    jobq = db.Column(db.String(255), nullable=True)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def get_model_id(self):
        return self.id

    @classmethod
    def delete_model(cls, model_id):
        model_job = cls.query.filter_by(id=model_id).first()
        db.session.delete(model_job)
        db.session.commit()