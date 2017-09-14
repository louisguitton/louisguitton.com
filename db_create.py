#!/home/louis/miniconda3/bin/python3.6
from app import db
from app.models import User

db.create_tables([User])
