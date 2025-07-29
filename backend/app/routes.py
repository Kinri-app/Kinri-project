# app/routes.py
from flask import Blueprint

# This blueprint wraps all API routes under the "/api" path
api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/")
def index():
    return {"message": "Kinri App Running!"}
