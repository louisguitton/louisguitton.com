from flask import Flask
from peewee import SqliteDatabase
from flask_login import LoginManager
from flask_oauthlib.client import OAuth, OAuthException

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'development'

db = SqliteDatabase(app.config['DATABASE_URI'])

lm = LoginManager(app)
lm.login_view = 'index'

oauth = OAuth(app)

from app import views, models
