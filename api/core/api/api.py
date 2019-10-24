"""api.py

Primary API provider.
"""
from api.db import ConnectionMiddleware
from api.sqlalchemy import get_engine

from api.resources import (
    ping,
)

#pylint: disable=import-error
import falcon
#pylint: enable=import-error

ENGINE = get_engine()

API = APPLICATION = falcon.API(
    middleware=[
        ConnectionMiddleware(ENGINE),
    ]
)

PING = ping.PingResource()

API.add_route('/ping', PING)
