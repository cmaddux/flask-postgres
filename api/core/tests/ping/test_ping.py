"""test_ping.py

Provides all basic tests for ping endpoints.
"""
import json

def test_get_ping(client):
    """Tests basic /ping endpoint"""
    expect = {
        'pong': True
    }

    response = client.get('/ping')
    result_doc = json.loads(response.data.decode('utf-8'))

    assert result_doc == expect
