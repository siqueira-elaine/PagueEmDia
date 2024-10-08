from datetime import datetime
import uuid
from sqlalchemy import func
from sqlalchemy.dialects.mysql import CHAR
from enum import Enum as PyEnum
from app import db

class SlipStatus(PyEnum):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELLED = "CANCELLED"

class Slip(db.Model):
    __tablename__ = 'slips'
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(CHAR(36), db.ForeignKey('users.id'), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    payment_date = db.Column(db.DateTime, nullable=True)
    value = db.Column(db.Float, nullable=True)
    status = db.Column(db.Enum(SlipStatus), default=SlipStatus.PENDING)
    description = db.Column(db.String(255), nullable=True)
    
    user = db.relationship('User', backref=db.backref('slips', lazy=True))
