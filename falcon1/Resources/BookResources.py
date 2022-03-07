import falcon
from falcon1.Resources.Versions.V2.Book import Book as V2
from falcon1.Resources.Versions.V1.Book import Book as V1
from falcon1.Hooks.VersionParameter import ValidateParameter

@falcon.before(ValidateParameter.validate_version, ['V1', 'V2'])
class Books:
    def on_get(self, req, resp, version):
        if version == 'V1':
            V1.on_get(req, resp)
        elif version == 'V2':
            V2().on_get(req=req, resp=resp)

    def on_get_book(self, req, resp, version, book_id):
        if version == 'V1':
            V1.on_get_book(req, resp, book_id)
        elif version == 'V2':
            V1.on_get_book(req, resp, book_id)

    def on_post(self, req, resp, version):
        if version == 'V1':
            V1.on_post(req, resp)
        elif version == 'V2':
            V1.on_post(req, resp)

    def on_put_book(self, req, resp, version, book_id):
        if version == 'V1':
            V1.on_put_book(req, resp, book_id)
        elif version == 'V2':
            V1.on_put_book(req, resp, book_id)
    
    def on_delete_book(self, req, resp, version, book_id):
        if version == 'V1':
            V1.on_delete_book(req, resp, book_id)
        elif version == 'V2':
            V1.on_delete_book(req, resp, book_id)
