from marshmallow import Schema, fields, validates, validate, validates_schema, ValidationError

from .utils import is_valid_arrayd
from .classes import SeatsHandler


class PassengerSerializer(Schema):
    seats = fields.List(fields.List(fields.Int(), required=True))
    ttl_passenger = fields.Int(required=True, validate=validate.Range(min=1))

    @validates("seats")
    def validate_seats(self, value):
        """
        Custom serializer validation for attribute `seats`
        """
        try:
            is_valid_arrayd(value, 2)
        except ValueError as err:
            raise ValidationError(str(err))

    @validates_schema
    def validate_ttl_passenger(self, data, **kwargs):
        """
        Validate available seats with ttl passenger
        """
        try:
            SeatsHandler.is_valid_passenger(
                data["seats"], data["ttl_passenger"])
        except ValueError as err:
            raise ValidationError(str(err))
