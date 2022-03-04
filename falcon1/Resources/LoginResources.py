import jwt
from falcon1.Models.LoginModel import User
import falcon
from sqlobject import AND

class Login:
    def on_post(self, req, resp):
        form = req.get_media()
        form_data = {}
        for part in form:
            form_data[part.name] = part.text
        user = User.select(AND(User.q.username == form_data['username'], User.q.password == form_data['password']))
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
