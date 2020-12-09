import os
from typing import Final

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEFAULT_PAGE_LIMIT: Final[int] = 3
SECRET_KEY: Final[str] = 'jwt_token'

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getcwd()}/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = SECRET_KEY


# BLUEPRINTS
from bookapi.views.v1 import api_v1
from bookapi.views.home import home

app.register_blueprint(home)
app.register_blueprint(api_v1)
