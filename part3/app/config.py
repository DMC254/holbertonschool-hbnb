class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SECRET_KEY = 'a-production-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pass@localhost/db_name'
