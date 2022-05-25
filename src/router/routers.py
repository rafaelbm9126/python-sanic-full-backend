from sanic import Sanic
from sanic.response import (
  json,
  html,
)

from core.app import App
from middleware.fire import Middleware

middleware = Middleware()

class Routers():
  app          = App()
  power: Sanic = None

  def __init__(self, power: Sanic):
    self.power = power
    power.add_route(self.index, '/', methods=['GET'])
    power.add_route(self.sigup, '/sigup', methods=['POST'])
    power.add_route(self.sigin, '/sigin', methods=['POST'])
    power.add_route(self.verify, '/verify', methods=['POST'])
    power.add_route(self.secure, '/secure', methods=['POST'])
  
  def index(self, request):
    return html('<h1>Welcome!</h1>', status=200)

  def sigup(self, request):
    body, status = self.app.application(self.app.sigup, request.json, None)
    return json(body, status=status)

  def sigin(self, request):
    body, status = self.app.application(self.app.sigin, request.json, None)
    return json(body, status=status)

  def verify(self, request):
    body, status = self.app.application(self.app.verify, None, request.token)
    return json(body, status=status)

  @middleware.authenticated
  def secure(self, request):
    body, status = self.app.application(self.app.secure, request.ctx, None)
    return json(body, status=status)
