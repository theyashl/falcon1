from sqlobject import *


class User(SQLObject):
    username = StringCol(length=30, notNone=True, unique=True)
    password = StringCol(length=30, notNone=True)

User.createTable(ifNotExists=True)