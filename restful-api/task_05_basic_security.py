#!/usr/bin/python3

"""
task_05_basic_security.py

Flask API implementing:
- Basic HTTP Authentication
- JWT-based authentication and role-based access control

Includes:
- In-memory user store with hashed passwords
- Custom JWT error handlers
- Routes protected by auth mechanisms

Author: [Ton Nom]
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.error_handler
def unauthorized():
    """Handles unauthorized access for HTTP Basic Auth.

    Returns:
        Response: JSON with 401 error message.
    """
    return jsonify({"error": "Unauthorized"}), 401

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify(username, password):
    """Verifies Basic Auth credentials.

    Args:
        username (str): Username provided by client.
        password (str): Password provided by client.

    Returns:
        str or None: Username if valid, else None.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected by Basic Auth.

    Returns:
        str: Success message if auth is valid.
    """
    return f"Basic Auth: Access Granted!"

@app.route('/login', methods=["POST"])
def login():
    """Login route to issue JWT token.

    Expects:
        JSON body with "username" and "password".

    Returns:
        JSON: JWT access token if credentials are valid.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def protected():
    """Route protected by JWT token.

    Returns:
        JSON: Access granted message if token is valid.
    """
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin():
    """Admin-only route protected by JWT and role check.

    Returns:
        str or JSON: Message if access granted, or 403 error.
    """
    current_user = get_jwt_identity()
    user_data = users.get(current_user)

    if not user_data or user_data.get("role") != "admin":
        return jsonify({"msg": "Admins only"}), 403
    return f"Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing JWT in request.

    Args:
        err (str): Error message.

    Returns:
        JSON: 401 error response.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid JWT.

    Args:
        err (str): Error message.

    Returns:
        JSON: 401 error response.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handles expired JWT.

    Args:
        jwt_header (dict): JWT header.
        jwt_payload (dict): JWT payload.

    Returns:
        JSON: 401 error response.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handles revoked JWT.

    Args:
        jwt_header (dict): JWT header.
        jwt_payload (dict): JWT payload.

    Returns:
        JSON: 401 error response.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handles request needing a fresh JWT.

    Args:
        jwt_header (dict): JWT header.
        jwt_payload (dict): JWT payload.

    Returns:
        JSON: 401 error response.
    """
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
