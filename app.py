<<<<<<< HEAD
peto = 'marico'

if peto == 'marico':
    print(f'peto es {peto}')
=======
import json
from flask import Flask, jsonify, request
from jsonschema import Draft7Validator, validators, ValidationError
import requests
from pymongo import MongoClient
import certifi
import uuid
import os

#from dotenv import load_dotenv, find_dotenv
import datetime
import traceback

app = Flask('endpoint principal')

FLASK_PORT = os.environ.get("FLASK_PORT")
FLASK_HOST = os.environ.get("FLASK_HOST")
FRONT_URL = os.environ.get("FRONT_URL")

#MONGO_URI = os.environ.get("MONGO_URI")
#MONGO_DB = os.environ.get("MONGO_DB")
#MONGO_COL = os.environ.get("MONGO_COL")

# ==== inicializar conexion con mongo ==== #
#client = MongoClient(MONGO_URI,
#                    tlsCAFile=ca)
#db = client[MONGO_DB]
#coll = db[MONGO_COL]

BaseVal = Draft7Validator
def is_datetime(checker, inst):
    return isinstance(inst, datetime.datetime)
date_check = Draft7Validator.TYPE_CHECKER.redefine('datetime', is_datetime)
Validator = validators.extend(BaseVal, type_checker=date_check)

#Actualizar un documento en Mongo
def updateDocument(collection, ID, GID, new_values):
    try:
        query = {'sessionId': ID,'globalSessionId': GID}
        set_new_values = {"$set": new_values}
        with open('src/schema/outgoing_schema.json', 'r') as file:
            schema = json.load(file)
        
        validatePayload(new_values, schema)
        x = collection.update_one(query, set_new_values)
        return True
    except ValidationError as e:
        return f"Invalid Mongo payload: {e.args[0]}"
    except:
        return "Error while updating document"

#Añadir un documento nuevo a mongo
def addDocument(collection, new_values):
    try:
        with open('src/schema/outgoing_schema.json', 'r') as file:
            schema = json.load(file)
        validatePayload(new_values, schema)
        x = collection.insert_one(new_values)
        return True
    except ValidationError as e:
        return f"Invalid Mongo payload: {e.args[0]}"
    except:
        return "Error while inserting document"

#Validar payloads
def validatePayload(payload, schema):
    validator = Validator(schema=schema)

    try:
        validator.validate(payload)
        return True
    except:
        errors = validator.iter_errors(payload)
        error_log = []

        for e in errors:
            if len(e.json_path) > 1:
                detail = 'on ' + e.json_path[2:]
            else:
                detail = ''

            error_log.append(f'{e.message} {detail}')
        raise ValidationError(error_log)

#Enviar payload a otro endpoint
def sendPayload(url, payload):
    try:
        payload_endpoint = {"sessionId":payload["sessionId"],
                            "language":payload["language"],
                            "textId": payload["textId"],
                            "textOut": payload["textOut"]}
        response=requests.post(url, json=payload_endpoint)
        
        #print("response code: "+ response.status_code)
        return "Connection succesful with "+ url
    except requests.exceptions.RequestException as err:
        print(err)
        return "Error in connection with "+ url


#aplicacion de flask
@app.route('/macros', methods=['POST'])
def macros():
    try:
        pass
    except:
        pass

@app.route('/historial', methods=['POST'])
def historial():
    try:
        pass
    except:
        pass

@app.route('/reps', methods=['POST'])
def updateReps():
    try:
        pass
    except:
        pass
>>>>>>> 687a43be6db4fa987d5b119de6f6f5653184f484
