#!/usr/bin/python3
"""The principal module"""
from flask import render_template, url_for, request, redirect, flash, session
from app.extensions import db
from app.main import bp
from app.models.data import User
from app.models.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@bp.app_errorhandler(404)
def error_404():
    return render_template('errors/404.html'), 404



@bp.app_errorhandler(500)
def error_500():
    return render_template('errors/500.html'), 500

@bp.route('/')
def index():
    return render_template('base.html')


# User Registration Api End Point
@bp.route('/register/', methods = ['GET', 'POST'])
def register():
    # Creating RegistrationForm class object
    form = RegisterForm(request.form)

    # Cheking that method is post and form is valid or not.
    if request.method == 'POST' and form.validate():

        # if all is fine, generate hashed password
        hashed_password = generate_password_hash(form.password.data)

        # create new user model object
        new_user = User(

            name = form.name.data, 

            username = form.username.data, 

            email = form.email.data, 

            password = hashed_password )

        # saving user object into data base with hashed password
        db.session.add(new_user)

        db.session.commit()

        flash('You have successfully registered', 'success')

        # if registration successful, then redirecting to login Api
        return redirect(url_for('login'))

    else:

        # if method is Get, than render registration form
        return render_template('register.html', form = form)
    
# Login API endpoint implementation
@bp.route('/login/', methods = ['GET', 'POST'])
def login():
    # Creating Login form object
    form = LoginForm(request.form)
    # verifying that method is post and form is valid
    if request.method == 'POST' and form.validate:
        # checking that user is exist or not by email
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            # if user exist in database than we will compare our database hased password and password come from login form 
            if check_password_hash(user.password, form.password.data):
                # if password is matched, allow user to access and save email and username inside the session
                flash('You have successfully logged in.', "success")

                session['logged_in'] = True

                session['email'] = user.email 

                session['username'] = user.username
                # After successful login, redirecting to home page
                return redirect(url_for('home'))

            else:

                # if password is incorrect , redirect to login page
                flash('Username or Password Incorrect', "Danger")

                return redirect(url_for('login'))
    # rendering login page
    return render_template('login.html', form = form)


@bp.route('/logout/')
def logout():
    # Removing data from session by setting logged_flag to False.
    session['logged_in'] = False
    # redirecting to home page
    return redirect(url_for('home'))
