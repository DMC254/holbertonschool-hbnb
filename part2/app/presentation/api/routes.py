from flask_restx import Api
from app.presentation.api.v1 import routes as v1_routes

def register_namespaces(app):
    api = Api(
        app,
        title='HBnB API',
        version='1.0',
        description='HBnB RESTful API'
    )

    # Register all v1 namespaces under /api/v1
    for ns in v1_routes.namespaces:
        api.add_namespace(ns, path='/api/v1' + ns.path)

    return api
