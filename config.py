import os

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'add-your-random-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.getcwd()}/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True


