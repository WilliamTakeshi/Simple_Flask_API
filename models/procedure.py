from db import db

class ProcedureModel(db.Model):
    __tablename__ = 'procedure'

    id = db.Column(db.Integer, primary_key=True)
    procedurelist_id = db.Column(db.Integer, db.ForeignKey(procedurelist.id), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey(appointment.id), nullable=False)
    discount_percent = db.Column(db.Integer, default=0)

    procedurelist = db.relationship('ProcedureNameModel')
    appointment = db.relationship('AppointmentModel')

    def __init__(self, procedure_id, appointment_id, discount_percent):
        self.procedure_id = procedure_id
        self.appointment_id = appointment_id
        self.discount_percent = discount_percent

    def json(self):
        return {'procedure_id': self.procedure_id, 'appointment_id': self.appointment_id, 'discount_percent': self.discount_percent}

    @classmethod
    def find_by_appointment_id(cls, appointment_id):
        return {'appointment_id': self.appointment_id, 
            'procedure': [procedure for procedure in cls.query.filter_by(name=name).all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
