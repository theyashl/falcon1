from falcon1.Models.AuthorModel import Author as AuthorModel
from sqlobject import LIKE, SQLObjectNotFound
import falcon


class GetAuthorStorage:
    def get_author_storage(author_id=None, name=''):
        if author_id is None:
            return AuthorModel.select(LIKE(AuthorModel.q.name, "%"+name+"%"))
        else:
            try:
                return AuthorModel.get(author_id)
            except SQLObjectNotFound:
                raise falcon.HTTPBadRequest(title='Wrong author id',
            description='Please provide valid author id to get info')
