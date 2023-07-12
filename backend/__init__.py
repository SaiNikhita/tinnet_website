from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from marshmallow import Schema, fields
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

class StructureAPI(Resource):
    def post(self):
        print(request.files['file'])
        all = [doc.to_dict() for doc in db_ref.stream()]
        return all

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Connect to firebase
cred = credentials.Certificate('backend/config.json')
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
db_ref = db.collection('files')

api.add_resource(StructureAPI, '/api/getVisualization', endpoint='getVisualization')