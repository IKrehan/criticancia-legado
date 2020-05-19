from flask import Blueprint, render_template, redirect, request, flash, url_for, send_file, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import date

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required


db = SQLAlchemy()
migrate = Migrate()
admin = Admin()
login = LoginManager()