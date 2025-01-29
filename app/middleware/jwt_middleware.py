from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from flask import abort


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verify JWT token
        verify_jwt_in_request()

        # Get the current user's identity and claims
        current_user = get_jwt_identity()
        claims = get_jwt()
        
        print(">current_user")
        print(current_user)
        print(">claims")
        print(claims)

        # Check if the user has the "admin" role
        if claims.get("role") != "admin":
            abort(403, description="Admin role required")

        return f(*args, **kwargs)

    return decorated_function
