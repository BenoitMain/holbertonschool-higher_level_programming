#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {
    "jane": {
    "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
    },
         "john": {
             "username": "john", "name": "John", "age": 30, "city": "New York"
             }
         }

#Root endpoint
@app.route("/", methods = ['GET'])
def home():
    return "Hello, Flask!"

#Data endpoint
@app.route("/data", methods = ['GET'])
def data():
    return jsonify(list(users.keys()))

#Root endpoint
@app.route("/status")
def status():
    return "OK"

#Status endpoint
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"})
    else:
        return jsonify(users[username])

#add_user endpoint
@app.route("/add_user", methods = ['POST'])
def creat_user():
    data = request.get_json()

    #Check username in data
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    #Add username in data
    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
