# app/auth/routes.py

from flask import Blueprint, request

from app.auth.models import TokenBlocklist
from app.core.database import db
from app.user.models import User
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
)
from app.core.utils import standard_response
from app.user.schemas import RegisterSchema, LoginSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}

    errors = RegisterSchema().validate(data)
    if errors:
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Validation failed",
            reason="Invalid fields in registration request",
            developer_message=str(errors),
            data={}
        )

    email = data["email"]
    password = data["password"]

    if User.query.filter_by(email=email).first():
        return standard_response(
            status="CONFLICT",
            status_code=409,
            message="User already exists",
            reason="Email is already registered",
            developer_message=f"Duplicate email: {email}",
            data={}
        )

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return standard_response(
        status="CREATED",
        status_code=201,
        message="User created successfully",
        reason="Valid registration request",
        developer_message=f"User created with ID {user.id}",
        data={"user_id": user.id}
    )


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}

    errors = LoginSchema().validate(data)
    if errors:
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Validation failed",
            reason="Missing or invalid login credentials",
            developer_message=str(errors),
            data={}
        )

    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return standard_response(
            status="UNAUTHORIZED",
            status_code=401,
            message="Invalid credentials",
            reason="Incorrect email or password",
            developer_message=f"Failed login for email: {email}",
            data={}
        )

    return standard_response(
        status="OK",
        status_code=200,
        message="Login successful",
        reason="Valid user credentials",
        developer_message=f"User ID {user.id} logged in",
        data={
            "access_token": create_access_token(identity=str(user.id)),
            "refresh_token": create_refresh_token(identity=str(user.id))
        }
    )


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)

    return standard_response(
        status="OK",
        status_code=200,
        message="Access token refreshed",
        data={"access_token": new_token}
    )

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()

    return standard_response(
        status="OK",
        status_code=200,
        message="Logout successful",
        reason="Token revoked",
        developer_message=f"JWT {jti} added to blocklist",
        data={}
    )