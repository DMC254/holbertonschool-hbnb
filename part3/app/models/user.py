from ..extensions import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column('password', db.String(128), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean, default=False)

@property
def password(self):
    raise AttributeError('Password is write-only.')

@password.setter
def password(self, plaintext_password):
    self._password_hash = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

def check_password(self, plaintext_password):
    return bcrypt.check_password_hash(self._password_hash, plaintext_password)

def to_dict(self):
    return {
        'id': self.id,
        'email': self.email,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'is_admin': self.is_admin
    }

from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Password is write-only.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email
            # Don’t expose password!
        }

from ..extensions import db
from .base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('Password is write-only.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
            # No password_hash exposed!
        }
