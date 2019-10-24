"""conftest.py

Sets up pytest tests.
"""
from api import api

#pylint: disable=import-error
import pytest
#pylint: enable=import-error

@pytest.fixture
def client():
    return api.API.test_client()
