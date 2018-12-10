from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dashboard = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

from config import Config

dashboard.config.from_object(Config)

db.init_app(dashboard)
migrate.init_app(dashboard, db)

from app import models
from app import routes

if __name__ == "__main__":
    dashboard.run(host='0.0.0.0', debug=False, port=5000)