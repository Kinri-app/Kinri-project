import pytest
from app import create_app
from app.core.database import db as _db
from flask_jwt_extended import decode_token


@pytest.fixture(scope="module")
def test_client():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret",
        "SECRET_KEY": "test-secret",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

    app = create_app(test_config)

    with app.test_client() as testing_client:
        with app.app_context():
            _db.create_all()
        yield testing_client
        with app.app_context():
            _db.drop_all()


def test_register_login_logout_flow(test_client):
    # Register user
    res = test_client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "Password123"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["status"] == "CREATED"
    assert "user_id" in data["data"]
    print("\n\033[92m✔ User registration successful\033[0m")  # Green check

    # Login user
    res = test_client.post("/auth/login", json={
        "email": "testuser@example.com",
        "password": "Password123"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert "access_token" in data["data"]
    assert "refresh_token" in data["data"]
    print("\033[92m✔ User login successful and tokens received\033[0m")

    access_token = data["data"]["access_token"]

    # Get user profile
    res = test_client.get("/user/profile", headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert res.is_json
    print("\033[92m✔ User profile retrieved successfully\033[0m")

    # Update user profile
    res = test_client.put("/user/profile", headers={
        "Authorization": f"Bearer {access_token}"
    }, json={"email": "updateduser@example.com"})
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "OK"
    assert data["data"]["user"]["email"] == "updateduser@example.com"
    print("\033[92m✔ User profile updated successfully\033[0m")
