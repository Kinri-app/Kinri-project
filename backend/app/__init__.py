# app/__init__.py

from flask import Flask
from flask_cors import CORS  # 🔥 Import CORS
from supabase import create_client, Client
from .core.config import Config
import os
from mistralai import Mistral
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

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
    frontend_url = app.config.get("FRONTEND_URL", "http://localhost:5173").rstrip("/")
    CORS(
        app,
        resources={r"/api/*": {"origins": frontend_url}},
        supports_credentials=True,
    )

    # Initialize the Supabase client using credentials from the config
    supabase = create_client(app.config["SUPABASE_URL"], app.config["SUPABASE_KEY"])

    # Initialize the Mistral client using credentials from the config
    mistral = Mistral(api_key=app.config["MISTRAL_API_KEY"])

    # Import and register blueprints
    from .user.routes import user_bp
    from .chat.routes import chat_bp
    from .routes import api_bp
    from .assessment.routes import assessment_bp
    from .vaultcards.routes import vaultcards_bp
    from .flashcards.routes import flashcards_bp
    from .sessions.routes import sessions_bp
    from .test_routes import test_bp

    # Register individual blueprints under the main /api prefix
    api_bp.register_blueprint(user_bp, url_prefix="/users")
    api_bp.register_blueprint(chat_bp, url_prefix="/chat")
    api_bp.register_blueprint(assessment_bp, url_prefix="/assessments")
    api_bp.register_blueprint(vaultcards_bp, url_prefix="/vaultcards")
    api_bp.register_blueprint(flashcards_bp, url_prefix="/flashcards")
    api_bp.register_blueprint(sessions_bp, url_prefix="/sessions")

    # Register the main API blueprint
    app.register_blueprint(api_bp)

    # Serve Swagger UI at /api/docs
    swagger_yaml_path = os.path.join(os.path.dirname(__file__), 'swagger.yaml')
    SWAGGER_URL = '/api/docs'
    API_URL = '/api/swagger.yaml'

    @app.route(API_URL)
    def swagger_yaml():
        with open(swagger_yaml_path, 'r') as f:
            return f.read(), 200, {'Content-Type': 'application/x-yaml'}

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Kinri API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(rule)

    return app
