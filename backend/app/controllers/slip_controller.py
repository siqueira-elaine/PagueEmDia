from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from app.models.user import User
from app.models.slip import Slip, SlipStatus
from app import db
from app.services.slip_service import get_slips_by_user, create_slip, update_slip, delete_slip

slip_bp = Blueprint('slip', __name__)

@slip_bp.route('/slips', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    if not all(key in data for key in ['value']):
        return jsonify({"msg": "Missing data"}), 400

    new_slip = create_slip(
        user_id=user.id,
        value=data['value'],
        description=data.get('description', '')
    )

    return jsonify({
        "id": str(new_slip.id),
        "value": new_slip.value,
        "description": new_slip.description,
        "status": new_slip.status.value
    }), 201

@slip_bp.route('/slips', methods=['GET'])
@jwt_required()
def get_all():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    slips = get_slips_by_user(user.id)

    return jsonify([{
        "id": str(slip.id),
        "due_date": slip.due_date.strftime('%Y-%m-%d %H:%M:%S') if slip.due_date else None,
        "payment_date": slip.payment_date.strftime('%Y-%m-%d %H:%M:%S') if slip.payment_date else None,
        "value": slip.value,
        "description": slip.description,
        "status": slip.status.value
    } for slip in slips]), 200

@slip_bp.route('/slips/<slip_id>', methods=['PUT'])
@jwt_required()
def update(slip_id):
    data = request.get_json()

    due_date = data.get('due_date')
    payment_date = data.get('payment_date')
    value = data.get('value')
    description = data.get('description')
    status = data.get('status')

    updated_slip = update_slip(
        slip_id,
        due_date,
        payment_date,
        value,
        description,
        status
    )

    if updated_slip:
        return jsonify({
            "id": str(updated_slip.id),
            "due_date": updated_slip.due_date.strftime('%Y-%m-%d %H:%M:%S') if updated_slip.due_date else None,
            "payment_date": updated_slip.payment_date.strftime('%Y-%m-%d %H:%M:%S') if updated_slip.payment_date else None,
            "value": updated_slip.value,
            "description": updated_slip.description,
            "status": updated_slip.status.value
        }), 200

    return jsonify({"msg": "Slip not found"}), 404

@slip_bp.route('/slips/<slip_id>', methods=['DELETE'])
@jwt_required()
def cancel(slip_id):
    deleted = delete_slip(slip_id)

    if deleted:
        return jsonify({}), 200

    return jsonify({"msg": "Slip not found"}), 404
