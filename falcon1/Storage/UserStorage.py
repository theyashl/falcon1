from falcon1.Models.LoginModel import User
from sqlobject import AND


class UserStorage:
    def get_user(username, password):
        user = User.select(AND(User.q.username == username, User.q.password == password))
        return user
