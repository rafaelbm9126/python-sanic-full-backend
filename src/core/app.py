import uuid
from auth.lock import Auth
from model.user import User as UserModel
from module.user import (
  SingUpSchema,
  SingInSchema,
)
from tools.str_to_sha256 import StrToSha256

class App:
  auth   = Auth()

  def application(self, function, params: dict, token: str):
    body   = {}
    status = 200
    try:
      
      if hasattr(params, 'error'):
        status = 403
        raise Exception(params.error)

      body, status = function(params, token)

    except Exception as error:
      status = 400 if status == 200 else status
      body   = { 'error': str(error) }
    finally:
      return body, status

  def sigup(self, params: dict, token: str):
    validated = SingUpSchema().validate(params)
    if len(validated) > 0:
      raise Exception(str(validated))

    password = StrToSha256(params.get('password'))
    del params['password']

    user = UserModel.create(id=str(uuid.uuid4()), password=password, **params)
    user.save()

    return {}, 200

  def sigin(self, params: dict, token: str):
    validated = SingInSchema().validate(params)
    if len(validated) > 0:
      raise Exception(str(validated))

    token, user = self.auth.lock(params)
    body        = {
      'token': token,
      'user': user,
    }

    return body, 200

  def verify(self, params: dict, token: str):
    body = self.auth.unlock(token)
    return body, 200

  def secure(self, params: dict, token: str):
    body = { 'message': 'Welcome {0}'.format(params.user['name']) }
    return body, 200
