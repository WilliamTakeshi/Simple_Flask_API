from db import db

class ClientModel(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(40))

    def __init__(self, cpf, name, birthday):
        self.cpf = cpf
        self.name = name
        self.birthday = birthday

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {'cpf': self.cpf, 'name': self.name, 'birthday': self.birthday}
