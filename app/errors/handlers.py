from flask import render_template
from app.errors import errors


@errors.app_errorhandler(404)
def error_404():
    return render_template('errors/404.html'), 404



@errors.app_errorhandler(500)
def error_500():
    return render_template('errors/500.html'), 500
