import os
from typing import Final

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig') 

db = SQLAlchemy(app)

# BLUEPRINTS
from bookapi.views.v1 import api_v1
from bookapi.views.home import home

app.register_blueprint(home)
app.register_blueprint(api_v1)
