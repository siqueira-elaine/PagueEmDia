import uuid
from sqlalchemy import func
from sqlalchemy.dialects.mysql import CHAR
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())