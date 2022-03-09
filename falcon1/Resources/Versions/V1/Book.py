import falcon
import json
from falcon1.Storage.BookStorage import BookStorage


class Book:
    def on_get(req, resp):
        result = []
        if req.params:
            book_name = req.get_param("name") or ''
            author_name = req.get_param("author") or ''
            books = BookStorage().get_book_storage(name=book_name, author=author_name)
            result = [book.get_dict() for book in books]
        else:
            for book in BookStorage().get_book_storage():
                result.append(book.get_dict())
        resp.media = {'Books': result}
        resp.status = falcon.HTTP_200

    def on_get_book(req, resp, book_id):
        book = BookStorage().get_book_storage(book_id)
        book = book.get_dict()
        resp.media = {'book': book}
        resp.status = falcon.HTTP_200

    
    def on_post(req, resp):
        request = json.loads(req.stream.read())
        resp.media = BookStorage.create_book_storage(request)
        resp.status = falcon.HTTP_200

    def on_put_book(req, resp, book_id):
        request = json.loads(req.stream.read())
        BookStorage().update_book_storage(book_id=book_id, data=request)            
        resp.media = {'book': BookStorage().get_book_storage(book_id=book_id).get_dict()}
        resp.status = falcon.HTTP_200
    
    def on_delete_book(req, resp, book_id):
        BookStorage().delete_book_storage(book_id=book_id)
        result = []
        for book in BookStorage().get_book_storage():
            result.append(book.get_dict())
        resp.media = {'Books': result}
        resp.status = falcon.HTTP_200
