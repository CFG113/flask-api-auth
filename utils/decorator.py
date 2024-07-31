from functools import wraps
from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except HTTPException as e:
            response = jsonify({"error": e.description})
            response.status_code = e.code
            return response
        except Exception as e:
            response = jsonify({"error": "Internal server error"})
            response.status_code = 500
            return response
    return decorated_function
