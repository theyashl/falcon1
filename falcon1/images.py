import json
from unicodedata import name
from .models import Books
# from . import app
import falcon


class Resource:

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.text = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

class Book:
    def on_get(self, req, resp):
        result = []
        for book in Books.select():
            result.append(book.get_dict())
        resp.text = json.dumps({'books': result})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request = json.loads(req.stream.read())
        book = Books(name=request["name"], author=request["author"], rent=request["rent"])
        resp.texr = json.dumps(book.get_dict())
        resp.status = falcon.HTTP_200

class OneBook:
    def on_get(self, req, resp, book_id):
        resp.text = json.dumps({'book': Books.select(book_id)[0].get_dict()})
        resp.status = falcon.HTTP_200


# app.add_route('/images', Resource())
# app.add_route('/api/v1/books', Book())
# app.add_route('/api/v2/book/{book_id}', OneBook())

