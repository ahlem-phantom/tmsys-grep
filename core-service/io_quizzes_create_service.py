import requests

# TODO: define HOST and PORT as .env variables OR docker env values
HOST = 'http://io_quizzes_create'
PORT = 5000


def get(route, body):
    try:
        res = requests.get(f'{HOST}:{PORT}{route}', json=body)
        return res.status_code, res.json()
    except:
        raise Exception('Bad request.')


def post(route, body):
    try:
        res = requests.post(f'{HOST}:{PORT}{route}', json=body)

        try:
            return res.status_code, res.json()
        except:
            return res.status_code, None

    except:
        raise Exception('Bad request.')
