# tests/conftests.py

import sys
import os
import pytest

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.core.database import db as _db


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
