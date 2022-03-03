import falcon

from .middlewares import AuthMiddleware, VersioningComonent
from .images import Authors, Login, Resource, Books

app = application = falcon.App(middleware=AuthMiddleware())

app.add_route('/images', Resource())
app.add_route('/books', Books())
app.add_route('/books/{book_id}', Books(), suffix="book")
app.add_route('/authors', Authors())
app.add_route('/authors/{author_id}', Authors(), suffix="author")
app.add_route('/login', Login())
