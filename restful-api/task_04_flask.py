#!/usr/bin/python3
"""
task_04_flask.py
A simple Flask API (in-memory users dictionary).
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: To avoid checker issues, do NOT include testing users in this dict.
# Keep it empty in the pushed code.
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user object if exists, else 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user from JSON body.
    Rules:
    - invalid JSON -> 400 {"error":"Invalid JSON"}
    - missing username -> 400 {"error":"Username is required"}
    - username exists -> 409 {"error":"Username already exists"}
    - success -> 201 {"message":"User added","user":{...}}
    """
    # If Content-Type isn't JSON or body isn't valid JSON, handle safely
    try:
        payload = request.get_json(silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if payload is None or not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the whole object as value (as required)
    users[username] = payload

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Optional: set host/port if needed, but default app.run() is fine.
    app.run()
