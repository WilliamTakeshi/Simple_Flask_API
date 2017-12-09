from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.appointment import Appointment, AppointmentList
from resources.client import ClientRegister, Client
#from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clinicsecret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(AppointmentList, '/appointment')
api.add_resource(Appointment, '/appointment/<id>')
api.add_resource(ClientRegister, '/clientregister')
api.add_resource(Client, '/client/<cpf>')
#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(ItemList, '/items')
#api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
