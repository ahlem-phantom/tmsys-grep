from flask import Flask, request, Response, json
from utils import extract_field_from_body
import io_service
import security

app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return Response("Server is running!", status=200, mimetype='application/json')


@app.route('/auth', methods=['GET'])
def auth():
    try:
        body = request.get_json()

        token = extract_field_from_body('token', body)

        data = security.jwt_decode(token)

        return Response(json.dumps(data), status=200, mimetype='application/json')

    except Exception as e:
        return Response(str(e), status=401, mimetype='application/json')


@app.route('/auth/login', methods=['POST'])
def login():
    try:
        body = request.get_json()

        email = extract_field_from_body('email', body)
        password = extract_field_from_body('password', body)

        data = {
            'email': email
        }

        _, user = io_service.get('/users', data)

        if not user['activated']:
            return Response('User is not activated.', status=400, mimetype='application/json')

        if not security.verify_password(user['password'], password):
            return Response('Incorrect password.', status=400, mimetype='application/json')

        data = {
            'id': user['id'],
            'email': user['email'],
            'nickname': user['nickname']
        }

        jwt_token = security.jwt_encode(data)

        data = {
            'token': jwt_token
        }

        return Response(json.dumps(data), status=200, mimetype='application/json')

    except Exception as e:
        return Response(str(e), status=400, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
