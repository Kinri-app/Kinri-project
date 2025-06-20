# app/user/routes.py

from flask import Blueprint, g
from app import supabase
from app.auth.decorators import requires_auth
from app.core.utils import standard_response

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
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Failed to fetch user data from database.",
            developer_message=str(response.error)
        )

    # Return the list of user records
    return standard_response(
        status="OK",
        status_code=200,
        message="User data retrieved successfully.",
        data={"users": response.data}
    )


@user_bp.route('/profile', methods=["GET"])
@requires_auth
def profile():
    """
    GET /user/profile
    Returns the profile information of the authenticated user.
    Requires a valid JWT token in the Authorization header.

    Returns:
        - 200: The user profile data in JSON format.
    """
    user = g.current_user
    return standard_response(
        status="OK",
        status_code=200,
        message="User profile retrieved successfully.",
        data={"user": user}
    )
