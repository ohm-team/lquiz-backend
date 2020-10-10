import sentry_sdk
import os
from sanic import Sanic
from sanic.response import json
from sentry_sdk.integrations.sanic import SanicIntegration


# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_SDN"),
#     integrations=[SanicIntegration()]
# )

app = Sanic()


@app.route("/generate_questions")
async def welcome_view(request):
    return json({"message": "Welcome to lquiz-backend API"})


@app.route("/")
async def welcome_view(request):
    return json({"message": "Welcome to lquiz-backend API"})


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
