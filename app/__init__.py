#!/usr/bin/python3
"""flask factory function"""

from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_app():
        return '<h1>TEST APPLICATION</h1>'


    return app
