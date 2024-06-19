from flask_restful import Resource, Api, reqparse
from app.utils import vigenere_encrypt, caesar_encrypt, caesar_decrypt, vigenere_decrypt
from app.models import User, EncryptionMethod, Session
import time

users = {}
methods = [
    {"id": 1, "caption": "Caesar", "json_params": "{}", "description": "Caesar Cipher"},
    {"id": 2, "caption": "Vigenere", "json_params": "{}", "description": "Vigenere Cipher"}
]
sessions = {}

class UserList(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', required=True, type=str)
        parser.add_argument('secret', required=True, type=str)
        args = parser.parse_args()
        login = args['login']
        secret = args['secret']

        if login in users:
            return {'message': 'User already exists'}, 400

        users[login] = User(login, secret)
        return {'message': 'User created successfully'}, 201

    def get(self):
        return [{'login': user.login} for user in users.values()], 200

class MethodList(Resource):
    def get(self):
        return methods, 200

class Encrypt(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', required=True, type=str)
        parser.add_argument('secret', required=True, type=str)
        parser.add_argument('method_id', required=True, type=int)
        parser.add_argument('data', required=True, type=str)
        parser.add_argument('params', type=dict)
        args = parser.parse_args()

        login = args['login']
        secret = args['secret']
        method_id = args['method_id']
        data = args['data']
        params = args['params'] or {}

        if login not in users or users[login].secret != secret:
            return {'message': 'Invalid login or secret'}, 401

        method = next((m for m in methods if m['id'] == method_id), None)
        if not method:
            return {'message': 'Invalid method_id'}, 400

        data = ''.join(filter(str.isalnum, data.upper()))

        start_time = time.time()
        if method_id == 1:
            shift = params.get('shift', 3)
            encrypted_data = caesar_encrypt(data, shift)
        elif method_id == 2:
            key = params.get('key', 'DEFAULTKEY')
            encrypted_data = vigenere_encrypt(data, key)
        else:
            return {'message': 'Invalid method_id'}, 400
        end_time = time.time()

        session_id = len(sessions) + 1
        session = Session(session_id, login, method_id, data, params, encrypted_data, 'success', start_time, end_time)
        sessions[session_id] = session

        return {'session_id': session_id, 'encrypted_data': encrypted_data}, 201

class SessionResource(Resource):
    def get(self, session_id):
        session = sessions.get(session_id)
        if not session:
            return {'message': 'Session not found'}, 404
        return session.to_dict(), 200

    def delete(self, session_id):
        parser = reqparse.RequestParser()
        parser.add_argument('login', required=True, type=str)
        parser.add_argument('secret', required=True, type=str)
        args = parser.parse_args()

        login = args['login']
        secret = args['secret']

        session = sessions.get(session_id)
        if not session:
            return {'message': 'Session not found'}, 404

        if session.user_id != login or users[login].secret != secret:
            return {'message': 'Invalid login or secret'}, 401

        del sessions[session_id]
        return {'message': 'Session deleted successfully'}, 200

def initialize_routes(api):
    api.add_resource(UserList, '/users')
    api.add_resource(MethodList, '/methods')
    api.add_resource(Encrypt, '/encrypt')
    api.add_resource(SessionResource, '/sessions/<int:session_id>')
