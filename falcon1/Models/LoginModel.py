from sqlobject import *
from falcon1 import conn


class User(SQLObject):
    _connection = conn
    username = StringCol(length=30, notNone=True, unique=True)
    password = StringCol(length=30, notNone=True)

User.createTable(ifNotExists=True)