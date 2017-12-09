from flask import Flask, jsonify, request

app = Flask(__name__)

appointments = [
    {
        'id': 1,
        'client_id': 1,
        'register_date': '2017-12-01 00:00:00',
        'begin_date': '2017-12-01 07:00:00',
        'end_date': '2017-12-01 12:00:00',
        'procedures': [
            {
                'name': 'consulta simples',
                'price': '59.99'
            }
        ]
    }
]

@app.route('/')
def home():
    return 'Hello, world'

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify({'appointments': appointments})

@app.route('/appointment/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    for appointment in appointments:
        if appointment['id'] == int(appointment_id):
            return jsonify(appointment)
    return jsonify({'message': 'agendamento não encontrado'})

@app.route('/appointment/<appointment_id>/procedures', methods=['GET'])
def get_appointment_procedure(appointment_id):
    for appointment in appointments:
        if appointment['id'] == int(appointment_id):
            return jsonify(appointment['procedures'])
    return jsonify({'message': 'agendamento não encontrado'})

@app.route('/appointment', methods=['POST'])
def create_appointment():
    request_data = request.get_json()
    new_appointment = {
        'clienttid': request_data['clienttid'],
        'begin_date': request_data['begin_date'],
        'end_date': request_data['end_date'],
        'procedures': []
    }
    appointments.append(new_appointment)
    return jsonify(new_appointment)

@app.route('/appointment/<id>', methods=['PUT'])
def update_appointment():
    pass

@app.route('/appointment', methods=['DELETE'])
def delete_appointment():
    pass

app.run(port=5000, debug=True)

