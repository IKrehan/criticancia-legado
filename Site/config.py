import os

file_path = os.path.abspath('db.sqlite3')

SECRET_KEY = '''a+Wt@Y/CbD_zSHF=.:T[~uM>"Cc5q-DXu6aL;sY@j;W953S99+P?*L}
xb<Y(jEQ8{q=HDC3*#yRpa#KUduHFF5UDz7[F+f'`W`zfFS]{nf>dkp7Ew.y9V2nnhh`r)_?'''

SQLALCHEMY_DATABASE_URI = "sqlite:////home/ikrehan/Documents/criticancia/Site/db.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS = False