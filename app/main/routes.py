#!/usr/bin/python3
"""The principal module"""
from flask import render_template

from app.main import bp


@bp.route('/')
def index():
    return render_template('base.html')