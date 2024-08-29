from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.services.user_service import createUser, getUserByUsername, verifyPassword


auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if getUserByUsername(username):
        return jsonify({'message': 'Username already exists'}), 400

    user = createUser(username, email, password)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = getUserByUsername(username)
    if user and verifyPassword(user.password, password):
        accessToken = create_access_token(identity=username)
        return jsonify({'accessToken': accessToken, 'userId': user.id}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
