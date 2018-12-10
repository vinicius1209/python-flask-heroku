import os
from app import dashboard

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cout << "Vinicius" << endl;'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(dashboard.instance_path, 'task_list.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False