from flask import Blueprint, render_template, redirect, request, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .extensions import login_user, logout_user, db
from .models import Adms

auth = Blueprint('auth', __name__)

@auth.route("/mucegoeh")
def Login():
    return render_template('admLogin.html')


@auth.route('/wBHepKTI', methods=['GET', 'POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Adms.query.filter_by(username=username).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.Login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect('/admin')

@auth.route("/admlogout")
def admLogout():
    logout_user()
    return "Logged Out"


# Temporary(remove when in production) =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['GET','POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')

    user = Adms.query.filter_by(username=name).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = Adms(username=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.Login'))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-