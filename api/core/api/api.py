"""api.py

Primary API provider.
"""
from api.sqlalchemy import get_engine

#pylint: disable=import-error
from flask import Flask, g
#pylint: enable=import-error

API = APPLICATION = Flask(__name__)

ENGINE = get_engine()

@API.before_request
def before_request():
    g.connection = ENGINE.connect()

@API.route('/ping')
def ping():
    return {'pong': True}

@API.after_request
def after_request(response):
    conn = g.connection
    if conn:
        conn.close()

    return response
