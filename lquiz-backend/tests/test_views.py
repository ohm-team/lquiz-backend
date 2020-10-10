import pytest

from lquiz-backend.app import app


class TestWelcomeView:

    @pytest.fixture
    def url(self):
        return app.url_for('welcome_view')

    async def test_create(self, test_cli, url):
        resp = await test_cli.get(url)
        assert resp.status == 200
        resp_json = await resp.json()
        assert resp_json['message'] == "Welcome to lquiz-backend API"
