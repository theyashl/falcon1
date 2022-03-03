from email.policy import default
import json
from sre_constants import IN
import jwt
from .models import Author, Book, User
import falcon
from sqlobject import SQLObjectNotFound, AND, LIKE


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

class Books:
    def on_get(self, req, resp):
        result = []
        if req.params:
            if req.get_param("name"):
                for book in Book.select(LIKE(Book.q.name, "%"+req.get_param("name")+"%")):
                    result.append(book.get_dict())
        else:
            for book in Book.select():
                result.append(book.get_dict())
        resp.text = json.dumps({'Book': result})
        resp.status = falcon.HTTP_200

    def on_get_book(self, req, resp, book_id):
        try:
            book = Book.get(book_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong book id',
            description='Please provide valid book id to get info')
        book = book.get_dict()
        resp.text = json.dumps({'book': book})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request = json.loads(req.stream.read())
        author = request["author_id"]
        book = Book(name=request["name"], author=author, rent=request["rent"])
        resp.texr = json.dumps(book.get_dict())
        resp.status = falcon.HTTP_200

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
            
        resp.text = json.dumps({'book': book_dict})
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
        resp.text = json.dumps({'Book': result})
        resp.status = falcon.HTTP_200

class Authors:
    def on_get(self, req, resp):
        result = []
        for author in Author.select():
            result.append(author.get_dict())
        resp.text = json.dumps({'Authors': result})
        resp.status = falcon.HTTP_200

    def on_get_author(self, req, resp, author_id):
        try:
            author = Author.get(author_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong author id',
            description='Please provide valid author id to get info')
        author = author.get_dict()
        resp.text = json.dumps({'author': author})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request = json.loads(req.stream.read())
        author = Author(name=request["name"])
        resp.texr = json.dumps(author.get_dict())
        resp.status = falcon.HTTP_200

    def on_put_author(self, req, resp, author_id):
        try:
            author = Author.get(author_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong author id',
            description='Please provide valid author id to get info')
        author = author.get_dict()
        request = json.loads(req.stream.read())
        for k, v in request.items():
            author[k] = v
        Author.get(author_id).set(name=author['name'])
            
        resp.text = json.dumps({'author': author})
        resp.status = falcon.HTTP_200
    
    def on_delete_author(self, req, resp, author_id):
        try:
            Author.delete(author_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong author id',
            description='Please provide valid author id to get info')
        result = []
        for author in Author.select():
            result.append(author.get_dict())
        resp.text = json.dumps({'Authors': result})
        resp.status = falcon.HTTP_200

class Login:
    def on_post(self, req, resp):
        form = req.get_media()
        form_data = {}
        for part in form:
            form_data[part.name] = part.text
        user = User.select(AND(User.q.username == form_data['username'], User.q.password == form_data['password']))
        if user.count() > 0:
            user = user[0]
            payload = {
                'user_id': user.id
            }
            secret = 'secret'
            algo = "HS256"
            encoded = jwt.encode(payload=payload, key=secret, algorithm=algo)
            resp.text = json.dumps({'token': encoded})
            resp.status = falcon.HTTP_200
        else:
            resp.text = json.dumps({"Error": "User Not Found"})
            resp.status = falcon.HTTP_200

# app.add_route('/images', Resource())
# app.add_route('/api/v1/Book', Book())
# app.add_route('/api/v2/book/{book_id}', OneBook())
