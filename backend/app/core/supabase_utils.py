# app/utils/supabase_utils.py

from app import supabase


def sync_user_with_supabase(payload):
    """
    Synchronizes an Auth0-authenticated user with the Supabase 'users' table.

    This function:
    - Extracts user information from the JWT payload.
    - Checks if a user with the given Auth0 ID already exists in Supabase.
    - If the user does not exist, it inserts a new record into the 'users' table.
    - Returns the user record (existing or newly created).

    Args:
        payload (dict): Decoded JWT token payload from Auth0, expected to contain:
            - "sub": The Auth0 user ID (required).
            - "email": The user's email (optional).
            - "name": The user's full name (optional, defaults to "API Client").

    Returns:
        dict: The user record from Supabase.

    Raises:
        Exception: If a Supabase error occurs during select or insert operations.
    """
    # Extract user fields from the token payload
    auth0_id = payload.get("sub")
    email = payload.get("email")
    name = payload.get("name", "API Client")

    # If no email is provided, create a placeholder email to satisfy DB constraints
    if not email:
        email = f"{auth0_id}@no-email.local"

    # Check if the user already exists in the Supabase 'users' table
    res = supabase.table("users").select("*").eq("auth0_id", auth0_id).execute()
    res_dict = res.dict()

    # Handle select query error
    if res_dict.get("error") is not None:
        raise Exception(f"Supabase error: {res_dict['error']}")

    data = res_dict.get("data")

    if not data:
        # Insert the new user if not found
        res = supabase.table("users").insert({
            "auth0_id": auth0_id,
            "email": email,
            "name": name
        }).execute()

        res_dict = res.dict()

        # Handle insert query error
        if res_dict.get("error") is not None:
            raise Exception(f"Insert error: {res_dict['error']}")

        return res_dict.get("data")[0]
    else:
        # Return the existing user
        return data[0]
