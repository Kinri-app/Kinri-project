# app/core/config.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment
load_dotenv()


class Config:
    """
    Application configuration class that loads secrets and keys from environment variables.

    These variables are expected to be defined in a `.env` file or set in the environment.
    This config is used throughout the app for authentication and third-party service integration.

    Attributes:
        AUTH0_DOMAIN (str): Your Auth0 tenant domain.
        AUTH0_AUDIENCE (str): The API audience identifier used to validate JWTs.
        AUTH0_CLIENT_SECRET (str): Client secret for machine-to-machine Auth0 authentication.
        AUTH0_CLIENT_ID (str): Client ID for the Auth0 application.

        SUPABASE_URL (str): The base URL of your Supabase project.
        SUPABASE_KEY (str): The Supabase API key used to access your project.

        SECRET_KEY (str): Flask secret key for sessions and other cryptographic features.
    """
    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")
    AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
    AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173/")

    SECRET_KEY = os.getenv("SECRET_KEY")
