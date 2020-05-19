import os

basedir = os.path.abspath(os.path.dirname(__file__))

IMAGE_UPLOAD = os.path.abspath(os.path.dirname(__file__))+ '\\static\\img\\banners'
UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__))+ '\\static\\uploads'
ALLOWED_IMAGE_EXTENSIONS = ['PNG', 'JPG', 'JPEG']

SECRET_KEY = '''a+Wt@Y/CbD_zSHF=.:T[~uM>"Cc5q-DXu6aL;sY@j;W953S99+P?*L}
xb<Y(jEQ8{q=HDC3*#yRpa#KUduHFF5UDz7[F+f'`W`zfFS]{nf>dkp7Ew.y9V2nnhh`r)_?'''

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

