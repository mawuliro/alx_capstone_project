#!/usr/bin/python3

"""Configuration module"""
import os

class Config:
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:roland@localhost/blogpostdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER') or 'mawuliro2001@gmail.com'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = True
