import json
from falcon1.Models.AuthorModel import Author
import falcon
from sqlobject import SQLObjectNotFound, IN

class Authors:
    def on_get(self, req, resp):
        result = []
        for author in Author.select():
            result.append(author.get_dict())
        resp.media = {'Authors': result}
        resp.status = falcon.HTTP_200

    def on_get_author(self, req, resp, author_id):
        try:
            author = Author.get(author_id)
        except SQLObjectNotFound:
            raise falcon.HTTPBadRequest(title='Wrong author id',
            description='Please provide valid author id to get info')
        author = author.get_dict()
        resp.media = {'author': author}
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request = json.loads(req.stream.read())
        author = Author(name=request["name"])
        resp.media = author.get_dict()
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
            
        resp.media = {'author': author}
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
        resp.media = {'Authors': result}
        resp.status = falcon.HTTP_200
