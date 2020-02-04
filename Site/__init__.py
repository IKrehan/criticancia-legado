from flask import Flask

from .extensions import db, admin, login
from .models import models, MyAdminIndexView, MyModelView, Posts, Adms, Podcasts
from .views import views
from .auth import auth


def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)


    db.init_app(app)

    admin.init_app(app, index_view=MyAdminIndexView())
    login.init_app(app)


    admin.add_view(MyModelView(Posts, db.session))
    admin.add_view(MyModelView(Podcasts, db.session))
    admin.add_view(MyModelView(Adms, db.session))

    app.register_blueprint(models)
    app.register_blueprint(views)    
    app.register_blueprint(auth)

    #execute db commands when the server is executed (toggle comment to use)
    # with app.app_context():
        # db.create_all()
        # a = Adms(username='Criticante007', password='sha256$tmFgjPS7$7db9cba81f974237ee61837eb650b6e6f3adc844a610fff295d23fdc2ce15df5')
        # db.session.add(a)
        # db.session.commit()

    return app
