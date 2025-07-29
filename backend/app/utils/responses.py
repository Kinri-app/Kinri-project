from flask import jsonify

def standard_response(
    status: str,
    status_code: int,
    message: str,
    data=None,
    reason=None,
    developer_message=None,
):
    response = {
        "status": status,
        "status_code": status_code,
        "message": message,
    }

    if reason:
        response["reason"] = reason
    if developer_message:
        response["developer_message"] = developer_message
    if data is not None:
        response["data"] = data

    return jsonify(response), status_code
