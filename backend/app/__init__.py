# app/__init__.py

from flask import Flask
from flask_cors import CORS  # 🔥 Import CORS
from supabase import create_client, Client
from .core.config import Config
import os
from mistralai import Mistral

# Global Supabase client instance used throughout the app
supabase: Client = None

# Global MistralAI client instance used throughout the app
mistral = None


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
    global mistral

    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Setup CORS for React frontend
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

    # Initialize the Supabase client using credentials from the config
    supabase = create_client(
        app.config['SUPABASE_URL'],
        app.config['SUPABASE_KEY']
    )

    # Initialize the Mistral client using credentials from the config
    mistral = Mistral(api_key=app.config['MISTRAL_API_KEY'])

    # Import and register blueprints
    from .user.routes import user_bp
    from .chat.routes import chat_bp
    from .routes import api_bp

    # Register individual blueprints under the main /api prefix
    api_bp.register_blueprint(user_bp, url_prefix='/users')
    api_bp.register_blueprint(chat_bp, url_prefix='/chat')

    # Register the main API blueprint
    app.register_blueprint(api_bp)

    return app
