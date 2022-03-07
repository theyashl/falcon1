import falcon
from falcon1.Resources.AuthorResources import Authors
from falcon1.Resources.BookResources import Books
from falcon1.Resources.LoginResources import Login
from falcon1.Middleware.AuthMiddleware import AuthMiddleware
from falcon1.Middleware.ResponseMiddleware import ResponseMiddleware
from .images import Resource

def get_app():
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])

    app.add_route('/images', Resource())
    app.add_route('/{version}/books', Books())
    app.add_route('/{version}/books/{book_id:int}', Books(), suffix="book")
    app.add_route('/{version}/authors', Authors())
    app.add_route('/{version}/authors/{author_id:int}', Authors(), suffix="author")
    app.add_route('/{version}/login', Login())

    return app
