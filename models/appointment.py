from db import db

class AppointmentModel(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    date_begin = db.Column(db.String(40), nullable=False)
    date_end = db.Column(db.String(40), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    client = db.relationship('ClientModel') 
    procedure = db.relationship('ProcedureModel', lazy='dynamic')

    def __init__(self, date_begin, date_end, client_id):
        self.date_begin = date_begin
        self.date_end = date_end
        self.client_id = client_id

    def json(self):
        return {
            'id': self.id, 
            'date_begin': self.date_begin, 
            'date_end': self.date_end, 
            'client_id': self.client_id,
            'procedure': [procedure.json() for procedure in self.procedure.all()]
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_client_id(cls, client_id):
        return cls.query.filter_by(client_id=client_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
