from flask import Flask, app
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

from .extensions import db, bcrypt

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    return app

from .api.users import users_bp

def create_app(config_class):
    ...
    app.register_blueprint(users_bp)
    return app

from .extensions import db, bcrypt, jwt

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from .api.users import users_bp
    app.register_blueprint(users_bp)

    return app

from .api.places import places_bp
from . api.reviews import reviews_bp

def create_app(config_class):
    ...
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    ...
    return app

from .api.amenities import amenities_bp

def create_app(config_class):
    ...
    app.register_blueprint(amenities_bp)
    ...
