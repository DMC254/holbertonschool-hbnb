from flask import Flask
from app.presentation.api.routes import register_namespaces

def create_app():
    app = Flask(__name__)
    register_namespaces(app)
    return app
