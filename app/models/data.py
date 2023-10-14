from app.extensions import db
from app.main import bp


# Create User Model which contains id [Auto Generated], name, username, email and password

class User(db.Model):

    __tablename__ = 'usertable'

    id = db.Column(db.Integer, primary_key=True)

    name= db.Column(db.String(15), unique=True)

    username = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256), unique=True)

@bp.before_app_first_request
def create_tables():
    db.create_all()
