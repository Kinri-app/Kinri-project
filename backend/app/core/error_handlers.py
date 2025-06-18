# app/core/error_handlers.py

from flask import jsonify
from werkzeug.exceptions import HTTPException
from app.core.utils import standard_response


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return standard_response(
            status=e.name.replace(" ", "_").upper(),
            status_code=e.code,
            message="An error occurred while processing your request.",
            reason=e.description,
            developer_message=f"{e.name} ({e.code}): {e.description}",
            data={}
        )

    @app.errorhandler(404)
    def handle_404(e):
        return standard_response(
            status="NOT_FOUND",
            status_code=404,
            message="The requested resource was not found.",
            reason="Invalid URL or endpoint",
            developer_message="404 Error: Endpoint does not exist",
            data={}
        )

    @app.errorhandler(500)
    def handle_500(e):
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An internal server error occurred.",
            reason="Unhandled exception in the backend",
            developer_message=str(e),
            data={}
        )

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return standard_response(
            status="UNEXPECTED_ERROR",
            status_code=500,
            message="An unexpected error occurred.",
            reason="A non-HTTP exception was raised",
            developer_message=str(e),
            data={}
        )
