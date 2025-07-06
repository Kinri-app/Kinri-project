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

    # Check if the user already exists
    res = supabase.table("users").select("*").eq("auth0_id", auth0_id).execute()
    res_dict = res.model_dump()

    if res_dict.get("error") is not None:
        raise Exception(f"Supabase error: {res_dict['error']}")

    data = res_dict.get("data")

    if not data:
        res = supabase.table("users").insert({
            "auth0_id": auth0_id
        }).execute()

        res_dict = res.model_dump()
        if res_dict.get("error") is not None:
            raise Exception(f"Insert error: {res_dict['error']}")

        return res_dict.get("data")[0]

    return data[0]
