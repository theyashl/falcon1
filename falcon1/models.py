from sqlobject import *
from . import conn
# Tues
# search books names author id name author
# author diff table

class Book(SQLObject):
    _connection = conn
    name = StringCol(length=30, notNone=True, unique=True)
    rent = IntCol(notNone=True)
    author = ForeignKey('Author', cascade=True)

    def get_dict(self):
        return {
            "name": self.name,
            "author": self.author.name,
            "rent": self.rent
        }

class Author(SQLObject):
    _connection = conn
    name = StringCol(length=30, notNone=True)
    books = MultipleJoin('Book')

    def get_dict(self):
        return {
            "name": self.name,
            "books": [book.name for book in Book.select(Book.q.author == self)]
        }

class User(SQLObject):
    _connection = conn
    username = StringCol(length=30, notNone=True, unique=True)
    password = StringCol(length=30, notNone=True)

Author.createTable(ifNotExists=True)
Book.createTable(ifNotExists=True)
User.createTable(ifNotExists=True)