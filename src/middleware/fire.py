from auth.lock import Auth

class Middleware:
  auth = Auth()

  def __init__(self,):
    pass

  def authenticated(self, func):
    def wrapper(*args, **kwargs):
      try:
        user = self.auth.unlock(args[1].token)
        args[1].ctx.user = user
      except Exception as error:
        args[1].ctx.error = str(error)
      return func(*args, **kwargs)
    return wrapper
