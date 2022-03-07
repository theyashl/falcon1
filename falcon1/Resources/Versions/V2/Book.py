import falcon
from falcon1.Hooks.BooksParameter import ValidateParameters
from falcon1.Storage.BookStorage import BookStorage
from falcon1.Resources.Versions.V1.Book import Book as V1


class Book:
    @falcon.before(ValidateParameters().validate_params)
    def on_get(self, req, resp):
        result = []
        if req.params:
            book_name = req.get_param("name") or ''
            author_name = req.get_param("author") or ''
            books = BookStorage().get_book_storage(name=book_name, author=author_name)
            result = [book.get_dict() for book in books]
            limit = req.get_param_as_int("limit") or len(result)
            result = result[:int(limit)]
        else:
            for book in BookStorage().get_book_storage():
                result.append(book.get_dict())
        resp.context.result = {'Books': result}
        resp.status = falcon.HTTP_200

    def on_get_book(self, req, resp, book_id):
        V1.on_get_book(req=req, resp=resp, book_id=book_id)

    def on_post(self, req, resp):
        V1.on_post(req=req, resp=resp)

    def on_put_book(self, req, resp, book_id):
        V1.on_put_book(req=req, resp=resp, book_id=book_id)

    def on_delete_book(self, req, resp, book_id):
        V1.on_delete_book(req=req, resp=resp, book_id=book_id)
