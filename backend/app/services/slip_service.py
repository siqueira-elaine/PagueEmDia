from app import db
from app.models.slip import Slip, SlipStatus
from datetime import datetime

def create_slip(user_id, value, description=None):
    new_slip = Slip(
        user_id=user_id,
        value=value,
        description=description,
        status=SlipStatus.PENDING
    )
    db.session.add(new_slip)
    db.session.commit()
    return new_slip

def get_slips_by_user(user_id):
    return Slip.query.filter_by(user_id=user_id).all()

def update_slip(slip_id, due_date=None, payment_date=None, value=None, description=None, status=None):
    slip = Slip.query.get(slip_id)
    
    if slip:
        if due_date:
            try:
                slip.due_date = datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Formato de data de vencimento inválido. Use 'YYYY-MM-DD'.")
        
        if payment_date:
            try:
                slip.payment_date = datetime.strptime(payment_date, '%Y-%m-%d')
                slip.status = SlipStatus.PAID
            except ValueError:
                raise ValueError("Formato de data de pagamento inválido. Use 'YYYY-MM-DD'.")
        
        slip.value = value if value is not None else slip.value
        slip.description = description if description is not None else slip.description
        slip.status = status if status is not None else SlipStatus.PENDING
        
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

def delete_slip(slip_id):
    slip = Slip.query.get(slip_id)

    if slip:
        db.session.delete(slip)
        db.session.commit()
        return True

    return False