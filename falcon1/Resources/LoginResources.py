import jwt
import falcon
from falcon1.Hooks.VersionParameter import ValidateParameter
from falcon1.Storage.UserStorage import UserStorage


@falcon.before(ValidateParameter.validate_version, ['V1', 'V2'])
class Login:
    def login_v1(self, req, resp):
        form = req.get_media()
        form_data = {}
        for part in form:
            form_data[part.name] = part.text
        user = UserStorage.get_user(username=form_data['username'], password=form_data['password'])
        if user.count() > 0:
            user = user[0]
            payload = {
                'user_id': user.id
            }
            secret = 'secret'
            algo = "HS256"
            encoded = jwt.encode(payload=payload, key=secret, algorithm=algo)
            resp.media = {'token': encoded}
            resp.status = falcon.HTTP_200
        else:
            resp.media = {"Error": "User Not Found"}
            resp.status = falcon.HTTP_200

    def login_v2(self, req, resp):
        self.login_v1(req, resp)

    def on_post(self, req, resp, version):
        if version == 'V1':
            self.login_v1(req, resp)
        elif version == 'V2':
            self.login_v2(req, resp)
