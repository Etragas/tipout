import logging
from argparse import ArgumentParser
import requests
from flask import Flask
import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi

class Application:
    def __init__(self, app, api_instance):
        logger.info("Initializing Application")
        self.app = app
        self.access_token = access_token
        self.api_instance = api_instance


logging.basicConfig(level=logging.DEBUG)
application = init()

@app.route('/')
def hello_world():
    return 'Get your tips out!'

def init():
    """ Initialize the app """
    parser = ArgumentParser()
    parser.add_argument(
        "--access-token-path", "-p"
        type=str, default="../appauth",
        description="Path to the Square access token"
    )
    args = parser.parse_args()

    # setup authorization
    with open(args.access_token_path) as token_file:
        squareconnect.configuration.access_token = token_file.read().strip()
    
    return Application(Flask(__name__), LocationsApi())
