#!/usr/bin/python3
"""creation of the user blueprint"""


from flask import Blueprint

users = Blueprint('users', __name__)

from app.users import routes
