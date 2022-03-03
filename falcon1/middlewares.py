import jwt
import falcon
# changes in falcon
from .models import User
from sqlobject import SQLObjectNotFound

class VersioningComonent:
    def process_request(self, req, resp):
        print(req.path)
# postman/insomia
class AuthMiddleware:

    def process_request(self, req, resp):
        if req.path == "/login":
            return
        token = req.get_header('Authorization')

        if token is None:
            description = ('Please provide an auth token '
                           'as part of the request.')

            raise falcon.HTTPUnauthorized(title='Auth token required',
                                          description=description,
                                          href='http://docs.example.com/auth')

        if not self._token_is_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized(title='Authentication required',
                                          description=description,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, token):
        try:
            payload = jwt.decode(token, "secret", algorithms="HS256")
            User.get(payload['user_id'])
            return True
        except (jwt.DecodeError, jwt.ExpiredSignatureError, SQLObjectNotFound):
            return False
