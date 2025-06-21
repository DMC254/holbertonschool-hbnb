from flask import Flask
from flask_restx import Api
from app.presentation.api.routes import api_namespace

def create_app():
    app = Flask(__name__)
    api = Api(app, title='HBnB API', version='1.0', description='HBnB Aplication API')

    #Register namespaces
    api.add_namespace(api_namespace)

    return app
