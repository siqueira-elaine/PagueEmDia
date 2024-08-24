from app import db, bcrypt
from app.models.user import User

def createUser(username, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def getUserByUsername(username):
    return User.query.filter_by(username=username).first()

def verifyPassword(storedPassword, providedPassword):
    return bcrypt.check_password_hash(storedPassword, providedPassword)