import sentry_sdk
import os
from sanic import Sanic
from sanic.response import json
from sentry_sdk.integrations.sanic import SanicIntegration

from .config import SENTRY_DSN


sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[SanicIntegration()]
)

app = Sanic()


@app.route("/number_question")
async def welcome_view(request):
    return json({"message": "Welcome to lquiz-backend API"})


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
