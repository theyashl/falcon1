from sqlobject import *
from . import conn

class Books(SQLObject):
    _connection = conn
    name = StringCol(length=30, notNone=True, unique=True)
    author = StringCol(length=30, notNone=True)
    rent = IntCol(notNone=True)

    def get_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "rent": self.rent
        }

Books.createTable(ifNotExists=True)