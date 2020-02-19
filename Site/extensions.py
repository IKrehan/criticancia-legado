from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user


db = SQLAlchemy()
migrate = Migrate()
admin = Admin()
login = LoginManager()