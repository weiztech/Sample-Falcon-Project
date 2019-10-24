from functools import wraps

from falcon import HTTPBadRequest

from marshmallow import ValidationError


def serializer_class(serializer):
    '''
    Decorator For Serializer Validation
    '''

    def inner_function(function):
        @wraps(function)
        def wrapper(api, req, *args, **kwargs):
            try:
                serializer.load(req.data)
            except ValidationError as err:
                raise HTTPBadRequest("Validation Error", err.messages)

            return function(api, req, *args, **kwargs)
        return wrapper

    return inner_function
