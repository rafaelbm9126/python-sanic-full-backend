from sanic import Sanic
from router.routers import Routers
import database.connection

power = Sanic(__name__)

Routers(power)

if __name__ == '__main__':
  power.run()
