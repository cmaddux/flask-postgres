"""ping.py

Provides resources associated with pinging API.
"""

#pylint: disable=too-few-public-methods
import json

#pylint: disable=import-error
import falcon
#pylint: enable=import-error

class PingResource:
    """PingResource class handles all requests
       associated with pinging API
    """
    def on_get(self, req, resp):
        """Handles get request to /ping

        Returns pong.
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'pong': True})
