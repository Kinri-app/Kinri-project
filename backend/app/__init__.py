# app/__init__.py

from flask import Flask
from supabase import create_client, Client
from .core.config import Config

# Global Supabase client instance used throughout the app
supabase: Client = None


def create_app():
    """
    Flask application factory function.

    This function initializes the Flask app and configures:
    - Environment-based settings from Config
    - The Supabase client for database and API interaction
    - The registration of blueprints for route organization

    Returns:
        Flask: The initialized Flask app instance
    """
    global supabase

    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Initialize the Supabase client using credentials from the config
    supabase = create_client(
        app.config['SUPABASE_URL'],
        app.config['SUPABASE_KEY']
    )

    # Import and register blueprints
    from .user.routes import user_bp

    app.register_blueprint(user_bp, url_prefix='/users')

    return app
