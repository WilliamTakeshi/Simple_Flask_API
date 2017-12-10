from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.appointment import Appointment, AppointmentList
from resources.client import ClientRegister, Client
from resources.procedurename import ProcedureName, ProcedureNameList
from resources.procedures import Procedure, ProcedureList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clinicsecret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(AppointmentList, '/v0/appointment')
api.add_resource(Appointment, '/v0/appointment/<_id>')
api.add_resource(ClientRegister, '/v0/client')
api.add_resource(Client, '/v0/client/<cpf>')
api.add_resource(UserRegister, '/v0/register')
api.add_resource(ProcedureNameList, '/v0/procedurename')
api.add_resource(ProcedureName, '/v0/procedurename/<_id>')
api.add_resource(ProcedureList, '/v0/procedure')
api.add_resource(Procedure, '/v0/procedure/<_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
