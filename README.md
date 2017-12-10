# Simple Flask API

## Overview

A simple flask REST API using Flask-RESTFul and SQLite

## Requeriments

Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy

## Design

The v0 API is formed by 5 tables.

* Appointment
* Client
* Procedure
* ProcedureList
* Users

## Appointment

They're identified by their ids, which are unique integers, and live under `/v0/appointment/<id>` or `/v0/appointment`.

All items have some of the following properties, with required properties in bold:

Field | Description
------|------------
**id** | The item's unique id. int
**date_begin** | The begin date of the appointment. str
**date_end** | The end date of the appointment. str
**client_id** | The id of the table client. int

The Appointment API have this properties

HTTP Method | Action | Examples
------|------------
GET | Obtain information about all appointments | /v0/appointment
POST | Post information about a appointments | /v0/appointment
GET | Obtain information about an appointment | /v0/appointment/<id>
PUT | Update information about an appointment | /v0/appointment/<id>
DELETE | Delete information about an appointment (need JWT Auth) | /v0/appointment/<id>


For example: GET {{url}}/v0/appointment/2

```javascript
{
    "id": 1,
    "date_begin": "2017-12-02 12:00:00",
    "date_end": "2017-12-02 13:00:00",
    "client_id": 3,
    "procedure": [
        {
            "id": 1,
            "procedurename_id": 1,
            "appointment_id": 1,
            "discount_percent": 15
        },
        {
            "id": 2,
            "procedurename_id": 2,
            "appointment_id": 1,
            "discount_percent": 30
        },
        {
            "id": 3,
            "procedurename_id": 3,
            "appointment_id": 1,
            "discount_percent": 0
        },
        {
            "id": 4,
            "procedurename_id": 4,
            "appointment_id": 1,
            "discount_percent": 0
        }
    ]
}
```

PS: The best practice is to add a new column called "flagDeleted" to delete an appointment.
PS1: The procedure is called by all procedures where the appointment_id = id

## Clients

Clients are identified by unique ids, and live under `/v0/client/` and `/v0/client/<cpf>` .

Field | Description
------|------------
**id** | The client's unique id. int
**cpf** | The client CPF. int
**name** | Full name. str
birthday | Birthday. str

The client API have this properties

HTTP Method | Action | Examples
------|------------
GET | Obtain information about all clients | /v0/client
POST | Create a new client | /v0/client
GET | Obtain information about a client | /v0/client/<cpf>

For example: GET {{url}}/v0/client/1

```javascript
{
    "client": [
        {
            "id": 1,
            "cpf": "12345678911",
            "name": "José da Silva",
            "birthday": null
        }
    ]
}
```

TODO: Add a block if len(cpf) != 11

## Procedure

Procedure are all procedure made in the history. Procedures are identified by unique ids, and live under `/v0/procedure/` and `/v0/procedure/<id>` .

Field | Description
------|------------
**id** | The procedure's unique id. int
**procedurename_id** | The id from procedurename's table. int
**appointment_id** | The id from appointment's table. int
discount_percent | Discount given in this procedure (%). float(precision=2)

The Procedure API have this properties

HTTP Method | Action | Examples
------|------------
GET | Obtain information about all procedure | /v0/procedure
POST | Post information about a procedure | /v0/procedure
GET | Obtain information about a procedure | /v0/procedure/<id>
PUT | Update information about a procedure | /v0/procedure/<id>
DELETE | Delete information about a procedure (need JWT Auth) | /v0/procedure/<id>

For example: GET {{url}}/v0/procedure/1

```javascript
{
    "id": 1,
    "procedurename_id": 1,
    "appointment_id": 1,
    "discount_percent": 15
}
```

TODO: Add a column named 'price' automatically calculated using the ProcedureName table and discount_percent.

## ProcedureName

ProcedureName is a table where all procedures made by a organization are listed. ProcedureNames are identified by unique ids, and live under `/v0/procedurename/` and `/v0/procedurename/<id>` .

Field | Description
------|------------
**id** | The procedure's unique id. int
**name** | Procedure's name. str
**price** | Procedure price. float(precision=2)

The procedure API have this properties

HTTP Method | Action | Examples
------|------------
GET | Obtain information about all procedures | /v0/procedurename
POST | Create a new procedures | /v0/procedurename
GET | Obtain information about a procedures | /v0/procedurename/<cpf>
PUT | Update information about a procedures | /v0/procedurename/<cpf>

For example: GET {{url}}/v0/procedurename

```javascript
{
    "procedure": [
        {
            "id": 1,
            "name": "consulta geral",
            "price": 60
        },
        {
            "id": 2,
            "name": "Raio X",
            "price": 70.5
        },
        {
            "id": 3,
            "name": "exame de sangue",
            "price": 100
        }
    ]
}
```


## Clients

Users are people who have access to the plataform. Users are identified by unique ids, and live under `/v0/register` and `/v0/auth` .

Field | Description
------|------------
**id** | The user's unique id. int
**username** | The username. str
**password** | User's password. str

The User API have this properties

HTTP Method | Action | Examples
------|------------
POST | Receive the JWT token | /v0/auth
POST | Register a new user | /v0/register


For example: POST {{url}}/v0/auth

if everything is correct

```javascript
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTI4ODM2NDUsImlhdCI6MTUxMjg4MzM0NSwibmJmIjoxNTEyODgzMzQ1LCJpZGVudGl0eSI6MX0.Y-o5Kfb1VyPRxpF3tMeQXvOYXwtB-kPvQdfyimaJeyw"
}
```

if the login fails

```javascript
{
    "description": "Invalid credentials",
    "error": "Bad Request",
    "status_code": 401
}
```

PS: This token has to be used with the Authorization header in the format JWT {{access_token}}