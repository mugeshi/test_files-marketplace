from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from .extensions import db, bcrypt
from datetime import datetime
import re

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)

    search_history = db.relationship('SearchHistory', backref='user')

    @validates('username')
    def validates_username(self, key, username):
        if not username:
          raise ValueError('No username provided')
        if len(username) < 3:
           raise ValueError('Username must be at least 3 characters long')
        return username


    @validates('email')
    def validates_email(self, key, email):
        if not email:
            raise ValueError('No email provided')
        if not self.is_valid_email(email):
            raise ValueError('Invalid email format')
        return email

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None


    @hybrid_property
    def password_hash(self):
        return self.password
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self.password = password_hash.decode('utf-8')
        
    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))


class SearchHistory(db.Model):
    __tablename__ = 'search_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String)
    search_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @validates('name')
    def validates_name(self, key, name):
        if not name:
            raise ValueError('No name provided')
        return name
