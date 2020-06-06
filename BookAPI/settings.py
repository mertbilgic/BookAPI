import os
from flask import Flask
from typing import Final

DEFAULT_PAGE_LIMIT: Final[int] = 3
SECRET_KEY: Final[str] = 'jwt_token'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getcwd()}/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = SECRET_KEY