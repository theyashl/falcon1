import falcon
from sqlobject import LIKE
from falcon1.Models.AuthorModel import Author as AuthorModel
from falcon1.Storage.AuthorStorage.GetAuthorStorage import GetAuthorStorage
from falcon1.Resources.Versions.V1.Author import Author as V1


class Author:
    def on_get(req, resp):
        result = []
        if req.params:
            author_name = req.get_param("name") or ''
            authors = GetAuthorStorage.get_author_storage(name=author_name)
            result = [author.get_dict() for author in authors]
            limit = req.get_param_as_int("limit") or len(result)
            result = result[:int(limit)]
        else:
            for author in GetAuthorStorage.get_author_storage():
                result.append(author.get_dict())
            result = [author.get_dict() for author in AuthorModel.select()]
        resp.context.result = {'Authors': result}
        resp.status = falcon.HTTP_200

    def on_post(req, resp):
        V1.on_post(req=req, resp=resp)
    
    def on_get_author(req, resp, author_id):
        V1.on_get_author(req=req, resp=resp, author_id=author_id)

    def on_put_author(req, resp, author_id):
        V1.on_put_author(req=req, resp=resp, author_id=author_id)

    def on_delete_author(req, resp, author_id):
        V1.on_delete_author(req=req, resp=resp, author_id=author_id)
