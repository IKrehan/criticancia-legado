from flask import Blueprint, render_template
from .extensions import db, UserMixin, current_user, ModelView, AdminIndexView

models = Blueprint('models', __name__)

class Adms(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    banner = db.Column(db.String(100))
    category = db.Column(db.String(100))

class Podcasts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    desc = db.Column(db.String(500))
    duration = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime)
    banner = db.Column(db.String(200))
    category = 'criticast'


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return render_template('adminfail.html')

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return render_template('adminfail.html')