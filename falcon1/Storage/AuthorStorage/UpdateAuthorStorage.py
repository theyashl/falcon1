from falcon1.Storage.AuthorStorage.GetAuthorStorage import GetAuthorStorage


class UpdateAuthorStorage:
    def update_author_storage(author_id=None, data={}):
        author = GetAuthorStorage.get_author_storage(author_id=author_id)
        author_dict = author.get_dict()
        for k, v in data.items():
            author_dict[k] = v
        author.set(name=author_dict['name'])
