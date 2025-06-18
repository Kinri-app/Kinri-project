# tests/test_auth.py

def test_user_registration(test_client):
    res = test_client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "Password123"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["status"] == "CREATED"
    assert "user_id" in data["data"]
    print("\n\033[92mUser registration successful\033[0m")


def test_user_login(test_client):
    res = test_client.post("/auth/login", json={
        "email": "testuser@example.com",
        "password": "Password123"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert "access_token" in data["data"]
    assert "refresh_token" in data["data"]
    test_auth_tokens.tokens = data["data"]  # Save for other tests
    print("\033[92mUser login successful and tokens received\033[0m")


def test_token_refresh(test_client):
    refresh_token = test_auth_tokens.tokens["refresh_token"]
    res = test_client.post("/auth/refresh", headers={
        "Authorization": f"Bearer {refresh_token}"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert "access_token" in data["data"]
    test_auth_tokens.tokens["new_access_token"] = data["data"]["access_token"]
    print("\033[92mAccess token refreshed successfully\033[0m")


def test_logout(test_client):
    access_token = test_auth_tokens.tokens["access_token"]
    res = test_client.post("/auth/logout", headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert res.status_code == 200
    print("\033[92mLogout completed and token revoked\033[0m")


def test_access_after_logout_should_fail(test_client):
    access_token = test_auth_tokens.tokens["access_token"]
    res = test_client.get("/user/profile", headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert res.status_code == 401
    print("\033[92mRevoked token correctly rejected after logout\033[0m")


# Helper object to share tokens between tests
class test_auth_tokens:
    tokens = {}
