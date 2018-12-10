import os
from app import dashboard

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cout << "Vinicius" << endl;'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False