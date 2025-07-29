# app/auth/utils.py

import requests
from app import Config
from jose import jwt

# Configuration variables for Auth0 integration
AUTH0_DOMAIN = Config.AUTH0_DOMAIN
API_AUDIENCE = Config.AUTH0_AUDIENCE
ALGORITHMS = ["RS256"]

# URL to fetch the JSON Web Key Set (JWKS) from Auth0
jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
jwks = requests.get(jwks_url).json()


def get_rsa_key(token):
    """
    Extracts the RSA public key from the JWKS that matches the token's key ID (kid).

    Args:
        token (str): JWT token string.

    Returns:
        dict or None: The RSA key dictionary if found, otherwise None.
    """
    header = jwt.get_unverified_header(token)
    for key in jwks["keys"]:
        if key["kid"] == header["kid"]:
            # Return the RSA key parameters needed to verify the JWT signature
            return {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    return None
