from flask_restx import Namespace, Resource

api_namespace = Namespace('main', description = 'Main API')

@api_namespace.route('/health')
class HealthCheck(Resource):
    def get(self):
        return {'status': 'OK'}
