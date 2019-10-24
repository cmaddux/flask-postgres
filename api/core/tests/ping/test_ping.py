"""test_ping.py

Provides all basic tests for ping endpoints.
"""
import json

#pylint: disable=import-error
import falcon
#pylint: enable=import-error

def test_get_ping(client):
    """Tests basic /ping endpoint"""
    expect = {
        'pong': True
    }

    response = client.simulate_get('/ping')
    result_doc = json.loads(response.content.decode('utf-8'))

    assert response.status == falcon.HTTP_200
    assert result_doc == expect
