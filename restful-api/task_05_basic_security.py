#!/usr/bin/python3
"""
task_05_basic_security.py
Basic Auth + JWT Auth + Role-based access control (RBAC) using Flask.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Secret key for JWT (for real apps, store securely in env vars)
app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users as specified
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# -----------------------------
# Basic Auth configuration
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT error handlers (MUST be 401)
# -----------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Missing Authorization header or wrong format
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Invalid signature, malformed token, etc.
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# (Optional but useful) If user claims/identity missing, still treat as auth error
@jwt.user_lookup_error_loader
def handle_user_lookup_error(jwt_header, jwt_payload):
    return jsonify({"error": "Missing or invalid token"}), 401


# -----------------------------
# JWT routes
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accept JSON payload: {"username":"user1","password":"password"}
    Return: {"access_token":"<JWT_TOKEN>"}
    """
    try:
        payload = request.get_json(silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not payload or not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    password = payload.get("password")

    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        # Credentials invalid -> 401
        return jsonify({"error": "Invalid credentials"}), 401

    # Put username as identity, and embed role as an extra claim
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


def _role_required(required_role):
    """
    Helper: check current user's role from stored users dict using identity.
    If token is valid but role not allowed -> 403.
    """
    username = get_jwt_identity()
    user = users.get(username)
    if not user or user.get("role") != required_role:
        return False
    return True


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    if not _role_required("admin"):
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
