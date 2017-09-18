from peewee import Model, BigIntegerField, CharField
from flask_login import UserMixin
from flask_admin.contrib.peewee import ModelView
# check flask admin for peewee here: https://github.com/flask-admin/flask-admin/blob/master/examples/peewee/app.py

from app import db


class BaseModel(Model):
    class Meta:
        database = db


class User(UserMixin, BaseModel):
    nickname = CharField(null=False)
    email = CharField(null=True)


class UserAdmin(ModelView):
    pass
