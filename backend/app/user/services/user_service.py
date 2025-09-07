# app/utils/user_service.py

from app import supabase


def sync_user_to_supabase(payload):
    """
    Synchronizes an Auth0-authenticated user with the Supabase 'users' table.

    This function:
    - Extracts the Auth0 user ID from the JWT payload.
    - Checks if a user with that ID exists in the Supabase 'users' table.
    - If not, inserts a new record with only the Auth0 ID.
    - Returns the user record.

    Args:
        payload (dict): Decoded JWT token payload from Auth0, expected to contain:
            - "sub": The Auth0 user ID (required).

    Returns:
        dict: The user record from Supabase.

    Raises:
        Exception: If a Supabase error occurs during select or insert.
    """
    auth0_id = payload.get("sub")
    if not auth0_id:
        raise ValueError("Missing 'sub' (Auth0 user ID) in token payload.")

    # Query Supabase to check if the user already exists by auth0_id
    res = supabase.table("users").select("*").eq("auth0_id", auth0_id).execute()

    # Check if the response data is None, indicating a possible error
    if res.data is None:
        raise Exception(f"Error fetching user from Supabase. Response: {res}")

    data = res.data

    # If user does not exist, insert a new record with auth0_id only
    if not data:
        res = supabase.table("users").insert({
            "auth0_id": auth0_id
        }).execute()

        # Check if insert operation was successful
        if res.data is None:
            raise Exception(f"Error inserting user into Supabase. Response: {res}")

        # Return the newly inserted user record
        return res.data[0]

    # Return the existing user record
    return data[0]