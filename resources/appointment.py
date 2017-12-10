from flask_restful import Resource, reqparse
from models.appointment import AppointmentModel

class Appointment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_begin',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('date_end',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('client_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, _id):
        appointment = AppointmentModel.find_by_id(_id)
        if appointment:
            return appointment.json()
        return {'message': 'Appointment not found'}, 404

    def delete(self, _id):
        appointment = AppointmentModel.find_by_id(_id)
        if appointment:
            appointment.delete_from_db()

        return {'message': 'Appointment deleted'}

    def put(self, _id):
        data = Appointment.parser.parse_args()
        appointment = AppointmentModel.find_by_id(_id)

        if appointment:
            appointment.date_begin = data['date_begin']
            appointment.date_end = data['date_end']
            appointment.client_id = data['client_id']
        else:
            appointment = AppointmentModel(**data)

        appointment.save_to_db()

        return appointment.json()

class AppointmentList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_begin',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('date_end',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('client_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self):
        return {'appointment': list(map(lambda x: x.json(), AppointmentModel.query.all()))}

    def post(self):
        data = Appointment.parser.parse_args()

        appointment = AppointmentModel(**data)
        try:
            appointment.save_to_db()
        except:
            return {"message": "An error occurred creating the appointment."}, 500

        return appointment.json(), 201
