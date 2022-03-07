from falcon1.Resources.Versions.V1.Author import Author as V1
from falcon1.Resources.Versions.V2.Author import Author as V2
import falcon
from falcon1.Hooks.VersionParameter import ValidateParameter


@falcon.before(ValidateParameter.validate_version, ['V1', 'V2'])
class Authors:
    def on_get(self, req, resp, version):
        if version == 'V1':
            V1.on_get(req, resp)
        elif version == 'V2':
            V2.on_get(req, resp)
    def on_get_author(self, req, resp, version, author_id):
        if version == 'V1':
            V1.on_get_author(req, resp, author_id)
        elif version == 'V2':
            V2.on_get_author(req, resp, author_id)

    def on_post(self, req, resp, version):
        if version == 'V1':
            V1.on_post(req, resp)
        elif version == 'V2':
            V2.on_post(req, resp)

    def on_put_author(self, req, resp, version, author_id):
        if version == 'V1':
            V1.on_put_author(req, resp, author_id)
        elif version == 'V2':
            V1.on_put_author(req, resp, author_id)
    
    def on_delete_author(self, req, resp, version, author_id):
        if version == 'V1':
            V1.on_delete_author(req, resp, author_id)
        elif version == 'V2':
            V1.on_delete_author(req, resp, author_id)
