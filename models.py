from peewee import *

from app import db


class City(Model):
    insee = CharField()
    name = CharField()
    postal_code = CharField()
    label = CharField()

    class Meta:
        database = db
