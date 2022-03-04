import falcon
from falcon1.Resources.AuthorResources import Authors
from falcon1.Resources.BookResources import Books
from falcon1.Resources.LoginResources import Login
from falcon1.Middleware.AuthMiddleware import AuthMiddleware
from .images import Resource

def get_app():
    app = falcon.App(middleware=AuthMiddleware())

    app.add_route('/images', Resource())
    app.add_route('/books', Books())
    app.add_route('/books/{book_id}', Books(), suffix="book")
    app.add_route('/authors', Authors())
    app.add_route('/authors/{author_id}', Authors(), suffix="author")
    app.add_route('/login', Login())

    return app
