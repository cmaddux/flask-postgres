"""db.py

Provides ConnectionMiddleware class.
"""

class ConnectionMiddleware:
    """ConnectionMiddleware exposes middleware handlers to attach a database
       connection to the context of every incoming request.
    """
    def __init__(self, Engine):
        self._engine = Engine

    def process_request(self, req, _):
        """process_request initializes a connection and attaches to request
           context for every incoming request
        """
        req.context.connection = self._engine.connect()

    def process_response(self, req, resp, resource, req_succeeded):
        """process_response closes the connection attached to request context
           for every outgoing response
        """
        req.context.connection.close()
