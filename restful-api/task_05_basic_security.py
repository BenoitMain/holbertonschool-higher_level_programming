#!/usr/bin/python3

# Importation des modules nécessaires pour Flask, Authentification et JWT
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth  # Authentification HTTP de base
from werkzeug.security import generate_password_hash, check_password_hash  # Pour hacher et vérifier les mots de passe
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity  # JWT

# Création de l'application Flask
app = Flask(__name__)

# Initialisation de l'authentification HTTP
auth = HTTPBasicAuth()

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401

# Clé secrète pour signer les tokens JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Initialisation de la gestion JWT avec Flask
jwt = JWTManager(app)

# Données utilisateurs simulées en mémoire (mot de passe hashé)
users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}

# Fonction de vérification du mot de passe pour l'auth basique
@auth.verify_password
def verify(username, password):
    # Vérifie que l'utilisateur existe et que le mot de passe correspond
    if username in users and check_password_hash(users[username]["password"], password):
        return username  # Renvoie l'utilisateur validé
    return None

# Route de test protégée par l'authentification de base
@app.route('/basic-protected', methods=["GET"])
@auth.login_required  # Nécessite une authentification HTTP Basic
def basic_protected():
    return f"Basic Auth: Access Granted!"  # Affiche le nom de l'utilisateur connecté

# Route de connexion pour recevoir un token JWT
@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()  # Récupère les données envoyées en JSON
    username = data.get("username")
    password = data.get("password")

    # Vérifie les identifiants
    if username in users and check_password_hash(users[username]["password"], password):
        # Prépare l'identité du token (on pourrait y ajouter d'autres infos, comme "role")
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)  # Retourne le token au client
    return jsonify({"msg": "Bad username or password"}), 401  # Échec d'auth

# Route protégée par JWT
@app.route('/jwt-protected', methods=["GET"])
@jwt_required()  # Nécessite un JWT valide dans les headers
def protected():
    return jsonify(message="JWT Auth: Access Granted")  # Répond avec confirmation

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin():
    current_user = get_jwt_identity()  # Récupère l'identité dans le token
    user_data = users.get(current_user)

    # Vérifier si l'utilisateur a un rôle admin
    if not user_data or user_data.get("role") != "admin":
        return jsonify({"msg": "Admins only"}), 403
    return f"Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# Démarrage du serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
