import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from project.api.users import users_blueprint

class Base(DeclarativeBase):
    pass


#INSTANTIATING THE DB HERE
db = SQLAlchemy()

def create_app(script_info=None):
    app = Flask(__name__)
    # SETTING CONFIG HERE
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(users_blueprint)
    app.shell_context_processor({'app': app, 'db': db})
    return app

