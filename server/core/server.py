from flask import Flask, request, Response, json
from utils import extract_field_from_body, generate_activation_token, get_user
import io_service
import email_service
import security

app = Flask(__name__)


@app.route('/api/status', methods=['GET'])
def status():
    return Response("Server is running!", status=200, mimetype='application/json')


@app.route('/api/users/activate/<token>', methods=['GET'])
def activate_user(token):
    try:

        data = {
            'token': token
        }

        code, _ = io_service.post('/users/activate', data)

        if code == 200:
            return Response('User activated.', status=201, mimetype='application/json')

        return Response('Bad request.', status=400, mimetype='application/json')

    except Exception as e:
        return Response(str(e), status=400, mimetype='application/json')


@app.route('/api/users', methods=['POST'])
def create_user():

    try:
        body = request.get_json()

        email = extract_field_from_body('email', body)
        password = extract_field_from_body('password', body)
        nickname = extract_field_from_body('nickname', body)

        if email == None:
            raise Exception('Field email is missing.')
        if password == None:
            raise Exception('Field password is missing.')
        if nickname == None:
            raise Exception('Field nickname is missing.')

        data = {
            'email': email,
            'password': security.hash_password(password),
            'nickname': nickname
        }

        code, res = io_service.post('/users', data)

        if code == 201:
            activation_token = generate_activation_token()

            data = {
                'user_id': res['id'],
                'token': activation_token
            }

            io_service.post('/activation_tokens', data)

            data = {
                'email': email,
                'token': activation_token
            }

            email_service.get('/', data)

            return Response(json.dumps(res), status=201, mimetype='application/json')

        return Response('Bad request.', status=400, mimetype='application/json')

    except Exception as e:
        return Response(str(e), status=400, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
