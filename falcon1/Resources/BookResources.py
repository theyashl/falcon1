import json
from falcon1.Models.AuthorModel import Author
from falcon1.Models.BookModel import Book
import falcon
from sqlobject import SQLObjectNotFound, LIKE, IN

class Books:
    def on_get(self, req, resp):
        result = []
        if req.params:
            book_name = req.get_param("name", default='')
            author_name = req.get_param("author", default='')
            for book in Book.select(LIKE(Book.q.name, "%"+book_name+"%")).filter(IN(Book.q.author, Author.select(LIKE(Author.q.name, "%"+author_name+"%")))):
                result.append(book.get_dict())
            limit = req.get_param("limit", default=len(result))
            result = result[:int(limit)]
            # if req.get_param("name"):
            #     for book in Book.select(LIKE(Book.q.name, "%"+req.get_param("name")+"%")):
            #         result.append(book.get_dict())
        else:
            for book in Book.select():
                result.append(book.get_dict())
        resp.media = {'Books': result}
        resp.status = falcon.HTTP_200

    def on_get_book(self, req, resp, book_id):
        try:
            book = Book.get(book_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong book id',
            description='Please provide valid book id to get info')
        book = book.get_dict()
        resp.media = {'book': book}
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request = json.loads(req.stream.read())
        author = request["author_id"]
        try:
            book = Book(name=request["name"], author=author, rent=request["rent"])
            resp.media = book.get_dict()
            resp.status = falcon.HTTP_200
        except Exception:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
            description="The data you provided cannot be proccessed! Try again")

    def on_put_book(self, req, resp, book_id):
        try:
            book = Book.get(book_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong book id',
            description='Please provide valid book id to get info')
        book_dict = book.get_dict()
        request = json.loads(req.stream.read())
        for k, v in request.items():
            book_dict[k] = v
        print(book_dict)
        try:
            Book.get(book_id).set(name=book_dict['name'], author=Author.get(book.author.id), rent=book_dict['rent'])
        except:
            raise falcon.HTTPBadRequest(title="Wrong info",
            description="Well it seems that you've provided wrong author id!")
            
        resp.media = {'book': book_dict}
        resp.status = falcon.HTTP_200
    
    def on_delete_book(self, req, resp, book_id):
        try:
            book = Book.get(book_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong book id',
            description='Please provide valid book id to get info')
        Book.delete(book_id)
        result = []
        for book in Book.select():
            result.append(book.get_dict())
        resp.media = {'Book': result}
        resp.status = falcon.HTTP_200
