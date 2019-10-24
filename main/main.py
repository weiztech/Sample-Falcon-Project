import falcon

from middlewares.parsers import JsonMiddleware
from passengers.api import PassengerSeats


# falcon API apps
app = falcon.API(middleware=[JsonMiddleware()])

# add API here
app.add_route('/', PassengerSeats())
