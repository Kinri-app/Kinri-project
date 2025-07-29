# app/auth/decorators.py

from functools import wraps
from flask import g
from app.auth.utils import get_rsa_key, ALGORITHMS, API_AUDIENCE, AUTH0_DOMAIN
from jose import jwt
from app.core.utils import standard_response
from app.user.services.user_service import sync_user_to_supabase


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

        auth = request.headers.get("Authorization", None)
        if not auth:
            return standard_response(
                status="UNAUTHORIZED",
                status_code=401,
                message="Missing Authorization header",
                reason="Authorization header is required",
                developer_message="No 'Authorization' header found in the request."
            )

        parts = auth.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            return standard_response(
                status="UNAUTHORIZED",
                status_code=401,
                message="Invalid Authorization header format",
                reason="Invalid token format",
                developer_message="Expected header format: 'Bearer <token>'"
            )

        token = parts[1]
        rsa_key = get_rsa_key(token)
        if rsa_key is None:
            return standard_response(
                status="UNAUTHORIZED",
                status_code=401,
                message="RSA key not found",
                reason="Token verification key not available",
                developer_message="Unable to find matching 'kid' in JWKS"
            )

        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
        except Exception as e:
            return standard_response(
                status="UNAUTHORIZED",
                status_code=401,
                message="Token validation failed",
                reason="Invalid JWT",
                developer_message=str(e)
            )

        user = sync_user_to_supabase(payload)
        g.current_user = user
        return f(*args, **kwargs)

    return wrapper
