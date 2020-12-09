from flask_sqlalchemy import SQLAlchemy
from bookapi import app

db = SQLAlchemy(app)

"""
    Create db model

    $python3
    >>> from dbmodel.user_model import db
    >>> db.create_all()
    >>> exit()

"""

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return str({
            'username':self.username,
            'password':self.password
        })

    def username_password_match(_username, _password):
        user = User.query.filter_by(username=_username).filter_by(password=_password).first()
        if user is None:
            return False
        else:
            return True

    def get_all_users():
        return User.query.all()

    def create_user(_username,_password):
        new_user = User(username=_username,password=_password)
        db.session.add(new_user)
        db.session.commit()

    
