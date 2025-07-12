from flask import Flask
from .config import Config
from .extensions import db  # If you have Flask extensions

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints here if you have them
    # from .api.users import users_bp
    # app.register_blueprint(users_bp, url_prefix='/api/v1/users')

    return app
