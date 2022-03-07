import falcon
from falcon1.Models.BookModel import Book as BookModel
from falcon1.Models.AuthorModel import Author as AuthorModel
from sqlobject import LIKE, IN, SQLObjectNotFound


class BookStorage:
    def get_book_storage(self, book_id=None, name='', author=''):
        if book_id is None:
            return BookModel.select(LIKE(BookModel.q.name, "%"+name+"%")).filter(IN(BookModel.q.author, AuthorModel.select(LIKE(AuthorModel.q.name, "%"+author+"%"))))
        else:
            try:
                return BookModel.get(book_id)
            except SQLObjectNotFound:
                raise falcon.HTTPBadRequest(title='Wrong book id',
            description='Please provide valid book id to get info')

    def update_book_storage(self, book_id=None, data={}):
        book = self.get_book_storage(book_id)
        book_dict = book.get_dict()
        for k, v in data.items():
            book_dict[k] = v
        try:
            book.set(name=book_dict['name'], author=AuthorModel.get(book.author.id), rent=book_dict['rent'])
        except:
            raise falcon.HTTPBadRequest(title="Wrong info",
            description="Well it seems that you've provided wrong author id!")
    
    def delete_book_storage(self, book_id):
        book = self.get_book_storage(book_id)
        BookModel.delete(book.id)
    
    def create_book_storage(data):
        try:
            book = BookModel(name=data["name"], author=data["author_id"], rent=data["rent"])
            return book.get_dict()
        except Exception:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
            description="The data you provided cannot be proccessed! Try again")
