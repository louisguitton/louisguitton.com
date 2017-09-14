from peewee import Model, BigIntegerField, CharField

from app import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = BigIntegerField(primary_key=True)
    nickname = CharField()
    email = CharField()

