import falcon
from .images import Resource, Book, OneBook

app = application = falcon.App()

app.add_route('/images', Resource())
app.add_route('/books', Book())
app.add_route('/books/{book_id}', OneBook())
