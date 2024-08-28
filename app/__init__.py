from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def createApp(config_class=None):
    app = Flask(__name__)

    if config_class is None:
        app.config.from_object('app.config.Config')
    else:
        app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.controllers import auth_controller
        from app.controllers import user_controller
        from app.controllers import slip_controller
        app.register_blueprint(auth_controller.auth_bp)
        app.register_blueprint(user_controller.user_bp)
        app.register_blueprint(slip_controller.slip_bp)

        db.create_all()

    return app