from flask import Blueprint

from .extensions import login_user, logout_user, db, render_template, redirect, request, flash, url_for, check_password_hash, generate_password_hash
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
    return redirect(url_for('views.home'))
