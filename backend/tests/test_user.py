# tests/test_user.py

import pytest


@pytest.fixture(scope="module")
def user_access_token(test_client):
    # Register a unique user for user tests
    email = "usertest@example.com"
    password = "Password123"

    res = test_client.post("/auth/register", json={"email": email, "password": password})
    assert res.status_code == 201

    # Login
    res = test_client.post("/auth/login", json={"email": email, "password": password})
    assert res.status_code == 200
    data = res.get_json()
    return data["data"]["access_token"]


def test_get_user_profile(test_client, user_access_token):
    res = test_client.get("/user/profile", headers={
        "Authorization": f"Bearer {user_access_token}"
    })
    assert res.status_code == 200
    print("\n\033[92mUser profile retrieved successfully\033[0m")


def test_update_user_profile(test_client, user_access_token):
    new_email = "userupdated@example.com"
    res = test_client.put("/user/profile", headers={
        "Authorization": f"Bearer {user_access_token}"
    }, json={"email": new_email})
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "OK"
    assert data["data"]["user"]["email"] == new_email
    print("\033[92mUser profile updated successfully\033[0m")

def test_delete_user_account(test_client, user_access_token):
    res = test_client.delete("/user/delete", headers={
        "Authorization": f"Bearer {user_access_token}"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "OK"
    assert "User account deleted successfully" in data["message"]
    print("\033[92mUser account deleted successfully\033[0m")
