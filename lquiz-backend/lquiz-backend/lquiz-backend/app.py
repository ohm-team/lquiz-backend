import sentry_sdk
import os
import sys
import json
import logging
import random
from sanic import Sanic
from sanic.response import json as jsonify
from sanic.exceptions import InvalidUsage, ServerError
from sanic_cors import CORS, cross_origin
from sentry_sdk.integrations.sanic import SanicIntegration

# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_SDN"),
#     integrations=[SanicIntegration()]
# )

logger = logging.getLogger(__name__)
app = Sanic()
CORS(app)


def load_questions():
    questions_by_locale_map = {}
    for questions_file in os.listdir("data"):
        with open(os.path.join("data", questions_file), encoding='utf-8') as f:
            locale = os.path.splitext(questions_file)[0].split("-")[1]
            questions_by_locale_map[locale] = json.load(f)["questions"]
            print(f"found {len(questions_by_locale_map[locale])} questions for locale {locale}")
    return questions_by_locale_map


questions_by_locale = load_questions()


def collect_questions(locale, size):
    question_set = questions_by_locale[locale]
    return random.sample(question_set, size)


@app.route("/generate_questions", methods=["GET"])
async def generate_questions(request):
    args = getattr(request, "args", None)
    logger.info(f"Got generate questions request with args {args}")
    args_dict = dict(args) if args else {}
    locale_arg = args_dict.get("locale", [])
    size_arg = args_dict.get("size", [])
    locale = locale_arg[0] if locale_arg else "en"
    size = size_arg[0] if size_arg else 20
    if "-" in locale:
        locale = locale.split("-")[0]
    if locale not in questions_by_locale:
        raise InvalidUsage(f"Invalid locale: {locale}")
    try:
        logger.info(f"Preparing set of {size} question in {locale} language")
        return jsonify({"questions": collect_questions(locale, size)}, ensure_ascii=False)
    except Exception as e:
        return ServerError("Couldn't prepare a set of questions")


@app.route("/")
async def welcome_view(request):
    return jsonify({"message": "Welcome to lquiz-backend API"})


if __name__ == "__main__":
    logging.basicConfig(
        handlers=[
            logging.FileHandler(os.getenv("LOG_FILE_PATH")),
            logging.StreamHandler()
        ],
        encoding='utf-8',
        level=os.getenv("LOG_LEVEL", "INFO"))
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
