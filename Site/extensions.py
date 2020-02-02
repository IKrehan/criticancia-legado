from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user
from werkzeug.utils import secure_filename


db = SQLAlchemy()
admin = Admin()
login = LoginManager()