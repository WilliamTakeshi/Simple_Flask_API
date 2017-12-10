from flask_restful import Resource, reqparse
from models.procedure import ProcedureModel
from flask_jwt import jwt_required

class Procedure(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('procedurename_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('appointment_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('discount_percent',
        type=float
    )

    def get(self, _id):
        procedure = ProcedureModel.find_by_id(_id)
        if procedure:
            return procedure.json()
        return {'message': 'Procedure not found'}, 404

    @jwt_required()
    def delete(self, _id):
        procedure = ProcedureModel.find_by_id(_id)
        if procedure:
            procedure.delete_from_db()
            return {'message': 'Procedure deleted'}

        return {'message': "There is no procedure with id '{}'".format(_id)}, 400

        
    def put(self, _id):
        data = Procedure.parser.parse_args()
        procedure = ProcedureModel.find_by_id(_id)

        if procedure:
            procedure.procedurename_id = data['procedurename_id']
            procedure.appointment_id = data['appointment_id']
            procedure.discount_percent = data['discount_percent']
        else:
            procedure = ProcedureModel(**data)

        procedure.save_to_db()

        return procedure.json()

class ProcedureList(Resource):

    def get(self):
        return {'procedure': [procedure.json() for procedure in ProcedureModel.query.all()]}

    def post(self):
        data = Procedure.parser.parse_args()

        procedure = ProcedureModel(**data)
        #try:
        procedure.save_to_db()
        #except:
        #    return {"message": "An error occurred creating the procedure."}, 500

        return procedure.json(), 201
