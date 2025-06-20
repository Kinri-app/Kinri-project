# app/user/routes.py

from flask import Blueprint, jsonify, g
from app import supabase
from app.auth.decorators import requires_auth

# Create a Flask Blueprint for user-related routes
user_bp = Blueprint('users', __name__)


@user_bp.route('/data')
@requires_auth
def get_user_data():
    """
    GET /user/data
    Returns all user records from the 'users' table in Supabase.

    This route is protected and requires a valid JWT token via the Authorization header.
    It uses the Supabase client to fetch all rows from the 'users' table.

    Returns:
        - 200: List of user records in JSON format.
        - 500: JSON with an error message if a Supabase query fails.
    """
    response = supabase.table('users').select('*').execute()

    # Handle possible errors from Supabase
    if hasattr(response, "error") and response.error:
        return jsonify({"error": str(response.error)}), 500

    # Return the list of user records
    return jsonify(response.data)


# Protected route to get the current user's profile information
@user_bp.route('/profile', methods=["GET"])
@requires_auth
def profile():
    """
    GET /users/profile
    Returns the profile information of the authenticated user.
    Requires a valid JWT token in the Authorization header.
    """
    user = g.current_user
    return jsonify(user)