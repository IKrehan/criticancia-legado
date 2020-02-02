from flask import Blueprint, render_template, redirect, request
from .extensions import login_user, logout_user
from .models import Adms

auth = Blueprint('auth', __name__)

@auth.route("/adm")
def Login():
    return render_template('admLogin.html')


@auth.route("/admlogin", methods=['GET' ,'POST'])
def admLogin():
    username = request.form['username']
    password = request.form['passsword']

    user = Adms.query.get(1)

    login_user(user)
    return redirect('/admin')


@auth.route("/admlogout")
def admLogout():
    logout_user()
    return "Logged Out"
