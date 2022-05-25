from math import lgamma
import os
import datetime
import jwt
from model.user import User as UserModel
from tools.str_to_sha256 import StrToSha256

class Auth:
  def prepare_to_print_user(self, users):
    user             = users[0]
    id               = str(user['id'])
    user['birthday'] = str(user['birthday'])
    del user['id']
    del user['password']
    return id, user

  def lock(self, params: dict):
    password = StrToSha256(params.get('password'))
    users = UserModel.select(UserModel).dicts().limit(1).where(
      UserModel.email == params.get('email'),
      UserModel.password == password,
    )

    if len(users) == 0:
      raise Exception('credentials not found')

    id, user = self.prepare_to_print_user(users)

    return jwt.encode(
      {
        'id': id,
        'exp' : datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=59)
      },
      os.environ.get('JWT_SECRET_KEY'),
      algorithm='HS256'
    ), user

  def unlock(self, token: str):
    obj_key = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms="HS256")

    users = UserModel.select(UserModel).dicts().limit(1).where(
      UserModel.id == obj_key.get('id')
    )

    if len(users) == 0:
      raise Exception('credentials not found')

    id, user = self.prepare_to_print_user(users)

    return user
