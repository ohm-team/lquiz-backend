import pytest

from lquiz-backend.app import app

@pytest.fixture
def test_cli(loop, test_client):
    return loop.run_until_complete(test_client(app))
