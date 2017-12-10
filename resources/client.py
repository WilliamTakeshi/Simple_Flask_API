from flask_restful import Resource, reqparse
from models.client import ClientModel

class ClientRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cpf',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('birthday',
        type=str
    )

    def get(self):
        return {'client': [client.json() for client in ClientModel.query.all()]}

    def post(self):
        data = ClientRegister.parser.parse_args()

        if ClientModel.find_by_cpf(data['cpf']):
            return {"message": "A client with that cpf already exists"}, 400

        user = ClientModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class Client(Resource):

    def get(self, cpf):
        client = ClientModel.find_by_cpf(cpf)
        if client:
            return client.json()
        return {"message": "A client with this cpf doesn't exists"}, 400