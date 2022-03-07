from falcon1.Models.AuthorModel import Author as AuthorModel
from falcon1.Storage.AuthorStorage.GetAuthorStorage import GetAuthorStorage


class DeleteAuthorStorage:
    def delete_author_storage(author_id):
        author = GetAuthorStorage.get_author_storage(author_id)
        AuthorModel.delete(author.id)