#!/usr/bin/python3

"""Configuration module"""
import os

class Config:
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = 'mysql://root:roland@localhost/blogpostdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
