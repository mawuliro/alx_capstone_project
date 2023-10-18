#!/usr/bin/python3
"""flask factory function"""

from flask import Flask
from config import Config
from app.extensions import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register blueprints here
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.posts import posts as posts_bp
    app.register_blueprint(posts_bp)

    from app.users import users as users_bp
    app.register_blueprint(users_bp)

    from app.errors import errors as errors_bp
    app.register_blueprint(errors_bp)


    return app
