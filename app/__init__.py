import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # ✅ Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.property import property_bp

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(property_bp)

    # ✅ AUTO-create database + tables
    with app.app_context():
        from app import models
        db.create_all()

    return app
