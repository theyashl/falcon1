from sqlobject import *


class Author(SQLObject):
    name = StringCol(length=30, notNone=True)
    books = MultipleJoin('Book')

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [book.name for book in Book.select(Book.q.author == self)]
        }

Author.createTable(ifNotExists=True)
from falcon1.Models.BookModel import Book
