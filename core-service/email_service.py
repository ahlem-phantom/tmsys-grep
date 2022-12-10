import requests

# TODO: define HOST and PORT as .env variables OR docker env values
HOST = 'http://email'
PORT = 5000


def get(route, body):
    try:
        requests.get(f'{HOST}:{PORT}{route}', json=body)
    except:
        raise Exception('Bad request.')
