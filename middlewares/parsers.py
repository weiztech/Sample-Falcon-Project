import json

from falcon import HTTPBadRequest


class JsonMiddleware(object):
    # allowed method for parsing request body to json
    ALLOWED_METHOD = ["PUT", "PATCH", "POST"]

    def process_request(self, req, resp):
        ''' 
        check json headers is valid and parsing json data, before routed to the API
        '''
        if req.method not in self.ALLOWED_METHOD:
            return

        if req.content_type != "application/json":
            raise HTTPBadRequest("JSON Format Not Found", "Found %s" %
                                 (req.content_type))

        data = req.bounded_stream.read(req.content_length or 0).decode("utf-8")
        if req.content_length:
            try:
                req.data = json.loads(data)
            except json.decoder.JSONDecodeError:
                raise HTTPBadRequest("Malformed JSON", "Invalid JSON Format")
