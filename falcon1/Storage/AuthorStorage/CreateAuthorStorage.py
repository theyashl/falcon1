from falcon1.Models.AuthorModel import Author as AuthorModel
import falcon


class CreateAuthorStorage:
    def create_author_storage(data):
        try:
            author = AuthorModel(name=data["name"])
            return author
        except Exception:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
            description="The data you provided cannot be proccessed! Try again")