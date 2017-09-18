from peewee import Model, BigIntegerField, CharField
from flask_login import UserMixin

from app import db


class BaseModel(Model):
    class Meta:
        database = db


class User(UserMixin, BaseModel):
    nickname = CharField(null=False)
    email = CharField(null=True)

