"""conftest.py

Sets up pytest tests.
"""

#pylint: disable=import-error
import pytest
from falcon import testing
#pylint: enable=import-error

from api.api import API

@pytest.fixture
def client():
    """client bootstraps the api as client for testing"""
    return testing.TestClient(API)
