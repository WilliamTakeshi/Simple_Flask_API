from flask_restful import Resource, reqparse
from models.procedurename import ProcedureNameModel
from flask_jwt import jwt_required

class ProcedureName(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, _id):
        procedurename = ProcedureNameModel.find_by_id(_id)
        if procedurename:
            return procedurename.json()
        return {'message': 'Procedure not found'}, 404
        
    def put(self, _id):
        data = ProcedureName.parser.parse_args()
        procedurename = ProcedureNameModel.find_by_id(_id)

        if procedurename:
            procedurename.name = data['name']
            procedurename.price = data['price']
        else:
            procedurename = ProcedureNameModel(**data)

        procedurename.save_to_db()

        return procedurename.json()

class ProcedureNameList(Resource):

    def get(self):
        return {'procedure': [procedure.json() for procedure in ProcedureNameModel.query.all()]}

    def post(self):
        data = ProcedureName.parser.parse_args()

        procedurename = ProcedureNameModel(**data)
        try:
            procedurename.save_to_db()
        except:
            return {"message": "An error occurred creating the procedure."}, 500

        return procedurename.json(), 201
