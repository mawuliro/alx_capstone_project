#!/usr/bin/python3
"""creation of the main blueprint"""


from flask import Blueprint

errors = Blueprint('errors', __name__)

from app.errors import handlers
