import json
import falcon
from falcon1.Storage.AuthorStorage.GetAuthorStorage import GetAuthorStorage
from falcon1.Storage.AuthorStorage.CreateAuthorStorage import CreateAuthorStorage
from falcon1.Storage.AuthorStorage.DeleteAuthorStorage import DeleteAuthorStorage
from falcon1.Storage.AuthorStorage.UpdateAuthorStorage import UpdateAuthorStorage


class Author:
    def on_get(req, resp):
        result = []
        for author in GetAuthorStorage.get_author_storage():
            result.append(author.get_dict())
        resp.media = {'Authors': result}
        resp.status = falcon.HTTP_200
    
    def on_get_author(req, resp, author_id):
        author = GetAuthorStorage.get_author_storage(author_id)
        resp.media = {'author': author.get_dict()}
        resp.status = falcon.HTTP_200

    def on_post(req, resp):
        request = json.loads(req.stream.read())
        author = CreateAuthorStorage.create_author_storage(data=request)
        resp.media = author.get_dict()
        resp.status = falcon.HTTP_200

    def on_put_author(req, resp, author_id):
        request = json.loads(req.stream.read())
        UpdateAuthorStorage.update_author_storage(author_id=author_id, data=request)
        resp.media = {'author': GetAuthorStorage.get_author_storage(author_id=author_id).get_dict()}
        resp.status = falcon.HTTP_200
    
    def on_delete_author(req, resp, author_id):
        DeleteAuthorStorage().delete_author_storage(author_id=author_id)
        result = []
        for author in GetAuthorStorage.get_author_storage():
            result.append(author.get_dict())
        resp.media = {'Authors': result}
        resp.status = falcon.HTTP_200
