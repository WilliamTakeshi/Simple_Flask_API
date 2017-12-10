from db import db

class ProcedureModel(db.Model):
    __tablename__ = 'procedure'

    id = db.Column(db.Integer, primary_key=True)
    procedurename_id = db.Column(db.Integer, db.ForeignKey('procedurename.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    discount_percent = db.Column(db.Float(precision=2), default=0.00)

    procedurename = db.relationship('ProcedureNameModel')
    appointment = db.relationship('AppointmentModel')

    def __init__(self, procedurename_id, appointment_id, discount_percent):
        self.procedurename_id = procedurename_id
        self.appointment_id = appointment_id
        self.discount_percent = discount_percent

    def json(self):
        return {'id': self.id, 'procedurename_id': self.procedurename_id, 'appointment_id': self.appointment_id, 'discount_percent': self.discount_percent}

    @classmethod
    def find_by_appointment_id(cls, appointment_id):
        query = cls.query.filter_by(appointment_id=appointment_id).first()
        return {'appointment_id': query.appointment_id, 
            'procedure': [procedure for procedure in cls.query.filter_by(name=name).all()]}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
