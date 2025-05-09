from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import jsonify

def roles_required(roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if 'role' in claims and claims['role'] in roles:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Insufficient permissions"), 403
        return decorator
    return wrapper
