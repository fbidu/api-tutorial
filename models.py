from peewee import *

db = SqliteDatabase("users.db")

class User(Model):
    email = CharField()
    birthday = CharField()

    class Meta:
        database = db

def create_tables():
    with db:
        db.create_tables([User])