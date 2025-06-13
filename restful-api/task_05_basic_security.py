#!/usr/bin/python3
"""Flask API server with authentication and authorization capabilities
Implements both Basic Auth and JWT token-based authentication"""

# Import required libraries
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

# Initialize Flask and authentication components
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Used for JWT signing
auth = HTTPBasicAuth()  # Basic auth handler
jwt = JWTManager(app)  # JWT handler

# In-memory user database with hashed passwords
users = {
    "user1": {
        "username": "user1",
        # Never store plain passwords
        "password": generate_password_hash("password"),
        "role": "user"  # Regular user role
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"  # Administrative role
    }
}


# Basic Authentication verification function
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


# Basic Auth protected endpoint
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Endpoint protected by Basic Authentication"""
    return "Basic Auth: Access Granted"


# Login endpoint for obtaining JWT token
@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns JWT token upon successful authentication"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Create JWT token with user identity and role
        access_token = create_access_token(
            identity={'username': username,
                      'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


# JWT protected endpoint
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT Authentication"""
    return "JWT Auth: Access Granted"


# Admin-only endpoint
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Endpoint restricted to users with admin role"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle when fresh token is required"""
    return jsonify({"error": "Fresh token required"}), 401


# Server startup
if __name__ == "__main__":
    app.run()
