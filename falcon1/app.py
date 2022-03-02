import falcon
from .images import Resource, Book, OneBook

app = application = falcon.App()

app.add_route('/images', Resource())
app.add_route('/api/v1/books', Book())
app.add_route('/api/{vers}/book/{book_id}', OneBook())
