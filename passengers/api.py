import json

from falcon import HTTP_200, HTTP_201

from common.request_validators import serializer_class

from .serializers import PassengerSerializer
from .classes import SeatsHandler


class PassengerSeats(object):
    serializers_class = {
        "on_post": PassengerSerializer()
    }

    def on_get(self, req, resp):
        """
        Handles GET requests
        """
        resp.status = HTTP_200
        resp.body = ('\nAmillary Passenger Seats Assignment - Jensen')

    @serializer_class(PassengerSerializer())
    def on_post(self, req, resp):
        """
        Handles Post
        """
        resp.status = HTTP_201
        resp.body = json.dumps(SeatsHandler(
            req.data["seats"], req.data["ttl_passenger"]).run())
