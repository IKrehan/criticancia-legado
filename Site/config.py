import os

db_path = os.path.abspath('Site/db.sqlite3').replace('\\', '/')
up_path = os.path.abspath('upload.txt').replace('\\', '/')

SECRET_KEY = '''a+Wt@Y/CbD_zSHF=.:T[~uM>"Cc5q-DXu6aL;sY@j;W953S99+P?*L}
xb<Y(jEQ8{q=HDC3*#yRpa#KUduHFF5UDz7[F+f'`W`zfFS]{nf>dkp7Ew.y9V2nnhh`r)_?'''

SQLALCHEMY_DATABASE_URI = f"sqlite:////{db_path}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = 'Site\static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp3'}

#print(db_path)