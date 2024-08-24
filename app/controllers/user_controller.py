from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<uuid:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify({
            "id": str(user.id),
            "username": user.username,
            "email": user.email
        }), 200

    return jsonify({"msg": "User not found"}), 404