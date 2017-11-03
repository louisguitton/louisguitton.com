from peewee import Model, BigIntegerField, CharField
from playhouse.shortcuts import model_to_dict

from flask import redirect, url_for, request
from flask_login import UserMixin, current_user
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
    def is_accessible(self):
        print(model_to_dict(current_user))
        print(current_user.is_authenticated)
        print(current_user.get_id())
        return current_user.is_authenticated #  and current_user.nickname == "louis_guitton"

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))
    pass
