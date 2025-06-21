from flask_restx import Namespace, Resource

api = Namespace('main', description='Main API')

@api.route('/health')
class HealthCheck(Resource):
    def get(self):
        return {'status': 'OK'}
