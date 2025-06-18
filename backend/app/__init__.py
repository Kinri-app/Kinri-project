# app/__init__.py

from flask import Flask
from app.core.config import Config
from app.core.database import db, migrate
from flask_jwt_extended import JWTManager

from app.core.error_handlers import register_error_handlers


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    jwt = JWTManager(app)

    from .routes import main
    from .auth.routes import auth_bp
    from .user.routes import user_bp

    app.register_blueprint(main)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app

