from datetime import datetime, timezone
from flask import jsonify


def standard_response(
        status: str,
        status_code: int,
        message: str,
        reason: str = None,
        developer_message: str = None,
        data: dict = None
):
    """
    Return a standardized JSON HTTP response.

    Args:
        status (str): HTTP status name, e.g. "OK", "BAD_REQUEST".
        status_code (int): HTTP status code, e.g., 200, 400.
        message (str): User-friendly message.
        reason (str, optional): Brief reason/context for the response.
        developer_message (str, optional): Additional details for developers.
        data (dict, optional): Additional payload data.

    Returns:
        Flask Response: JSON response with standard format.
    """
    response_body = {
        "timeStamp": datetime.now(timezone.utc).isoformat() + "Z",
        "status": status,
        "statusCode": status_code,
        "message": message,
        "reason": reason if reason else None,
        "developerMessage": developer_message if developer_message else None,
        "data": data if data else None
    }

    return jsonify(response_body), status_code