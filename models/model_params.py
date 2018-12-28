from models import db


class ModelParams(db.Model):

    __tablename__ = 'model_params'

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    i = db.Column(db.DECIMAL, primary_key=True, nullable=True)
    j = db.Column(db.DECIMAL, primary_key=True, nullable=True)
    k = db.Column(db.DECIMAL, primary_key=True, nullable=True)
    acc = db.Column(db.DECIMAL, nullable=True)

    @classmethod
    def get_params(cls, model_id):
        records = cls.query.filter_by(id=model_id).all()
        result = []
        for raw_object in records:
            raw_dictionary = raw_object.__dict__
            res_row = {"i": float(raw_dictionary["i"]),
                       "j": float(raw_dictionary["j"]),
                       "k": float(raw_dictionary["k"]),
                       "acc": float(raw_dictionary["acc"])}
            result.append(res_row)
        return result
