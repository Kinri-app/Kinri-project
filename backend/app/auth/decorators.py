# app/auth/decorators.py

from functools import wraps
from flask import jsonify, g
from app.auth.utils import get_rsa_key, ALGORITHMS, API_AUDIENCE, AUTH0_DOMAIN
from app.core.supabase_utils import sync_user_with_supabase
from jose import jwt


def requires_auth(f):
    """
    Decorator function to protect routes by requiring a valid JWT bearer token.

    This decorator:
    - Checks for the Authorization header in the incoming request.
    - Validates the token format ("Bearer <token>").
    - Retrieves the RSA key for verifying the token signature.
    - Decodes and verifies the JWT token with Auth0 parameters.
    - Synchronizes the authenticated user with Supabase.
    - Stores the user info in Flask's `g.current_user` for use inside the route.
    - Returns HTTP 401 if any step fails.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        from flask import request

        # Get Authorization header
        auth = request.headers.get("Authorization", None)
        if not auth:
            return jsonify({"message": "Missing Authorization header"}), 401

        parts = auth.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            return jsonify({"message": "Invalid Authorization header"}), 401

        token = parts[1]
        rsa_key = get_rsa_key(token)
        if rsa_key is None:
            return jsonify({"message": "RSA key not found"}), 401

        try:
            # Decode and validate the JWT token
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
        except Exception as e:
            return jsonify({"message": f"Token validation error: {str(e)}"}), 401

        # Sync user info with Supabase database
        user = sync_user_with_supabase(payload)
        # Store user in Flask's global context for the request
        g.current_user = user

        # Call the wrapped route function
        return f(*args, **kwargs)

    return wrapper
