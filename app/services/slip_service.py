from app import db
from app.models.slip import Slip, SlipStatus
from datetime import datetime

def create_slip(user_id, due_date, value, description=None):
    new_slip = Slip(
        user_id=user_id,
        due_date=due_date,
        value=value,
        description=description,
        status=SlipStatus.PENDING
    )
    db.session.add(new_slip)
    db.session.commit()
    return new_slip

def get_slips_by_user(user_id):
    return Slip.query.filter_by(user_id=user_id).all()

def update_slip(slip_id, due_date, value, description=None):
    slip = Slip.query.get(slip_id)
    if slip:
        slip.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        slip.value = value
        slip.description = description
        db.session.commit()
        return slip
    return None

def cancel_slip(slip_id):
    slip = Slip.query.get(slip_id)
    if slip:
        slip.status = SlipStatus.CANCELLED
        db.session.commit()
        return slip
    return None