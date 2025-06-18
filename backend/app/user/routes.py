from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.user.models import User
from app.core.database import db
from app.core.utils import standard_response

from app.user.schemas import UpdateUserSchema

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)

    if not user:
        return standard_response(
            status="NOT_FOUND",
            status_code=404,
            message="User not found",
            reason="The requested user ID does not exist in the database",
            developer_message=f"No user record found for ID {user_id}",
        )

    return standard_response(
        status="OK",
        status_code=200,
        message="User profile retrieved successfully",
        reason="User is authenticated and data is accessible",
        developer_message=f"User profile retrieved for ID {user.id}",
        data={
            "user": {
                "id": user.id,
                "email": user.email,
                "createdAt": user.created_at.isoformat()
            }
        }
    )


@user_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)

    if not user:
        return standard_response(
            status="NOT_FOUND",
            status_code=404,
            message="User not found",
            reason="No user found for update operation",
            developer_message=f"User ID {user_id} not found in database",
        )

    data = request.json or {}

    try:
        validated_data = UpdateUserSchema().load(data)
    except ValidationError as err:
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Validation failed",
            reason="Invalid input for profile update",
            developer_message=str(err.messages),
            data={}
        )

    email = validated_data.get("email")
    password = validated_data.get("password")

    if email:
        existing = User.query.filter(User.email == email, User.id != user.id).first()
        if existing:
            return standard_response(
                status="CONFLICT",
                status_code=409,
                message="Email is already in use",
                reason="Email provided is already registered by another user",
                developer_message=f"Email conflict during update for user ID {user_id}",
            )
        user.email = email

    if password:
        user.set_password(password)

    db.session.commit()

    return standard_response(
        status="OK",
        status_code=200,
        message="User profile updated successfully",
        reason="Valid fields received and saved",
        developer_message=f"User ID {user.id} updated with new data",
        data={
            "user": {
                "id": user.id,
                "email": user.email
            }
        }
    )


@user_bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete_account():
    user_id = get_jwt_identity()
    user = db.session.get(User, user_id)

    if not user:
        return standard_response(
            status="NOT_FOUND",
            status_code=404,
            message="User not found",
            reason="Cannot delete a non-existent user",
            developer_message=f"Delete attempted for non-existent user ID {user_id}",
            data={}
        )

    db.session.delete(user)
    db.session.commit()

    return standard_response(
        status="OK",
        status_code=200,
        message="User account deleted successfully",
        reason="Account deleted by authenticated user",
        developer_message=f"User ID {user_id} was deleted from database",
        data={}
    )
