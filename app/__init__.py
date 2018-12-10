from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    dashboard = Flask(__name__)

    from config import Config

    dashboard.config.from_object(Config)
    db.init_app(dashboard)
    migrate.init_app(dashboard, db)

    from app import models
    from app import routes

    dashboard.register_blueprint(routes.bp)

    return dashboard
