import sentry_sdk
import os
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
from sentry_sdk.integrations.sanic import SanicIntegration


# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_SDN"),
#     integrations=[SanicIntegration()]
# )

app = Sanic()
CORS(app)


def load_questions_set():
    pass


def collect_questions(locale, size):
    pass


@app.route("/generate_questions", methods=["GET"])
async def generate_questions(request):

    # query_args = dict(request.get_query_args())
    # locale = query_args.get("locale", "en")
    # size = query_args.get("count", 20)
    try:
        # return json(collect_questions(locale, size))
        return json(
            {
                "questions": [
                    {
                        "question": {
                            "whatStatistics": "Road traffic injuries by month in 2018 statistics for 1991 year:",
                            "whatValue": "Total victims killed amount is {value}",
                            "value": 83,
                            "imgSrc": "https://source.unsplash.com/random?quiz&version=0",
                            "correctAnswerId": "3",
                            "url": "https://data.public.lu/fr/datasets/r/7acd5f82-4bd3-4315-b067-3504a078b47b",
                            "answerUrl": "https://data.public.lu/fr/datasets/r/5d72fede-f8b9-4b1f-a1bb-8479787aafd9"
                        },
                        "id": "0",
                        "answers": [
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "1,000 tonne-kilometers amount in 1970",
                                "id": "0"
                            },
                            {
                                "answerStatistics": "by Results of the exams for obtaining a driving license 1991 - 2018 statistics",
                                "answerValue": "failed amount in 2012",
                                "id": "1"
                            },
                            {
                                "answerStatistics": "by Bodily accidents according to their nature 1991 - 2018 statistics",
                                "answerValue": "Collision between a vehicle and a tree amount in 2014",
                                "id": "2"
                            },
                            {
                                "answerStatistics": "by Interventions and number of firefighters 2013 - 2016 statistics",
                                "answerValue": "Total First Responder interventions amount in 2015",
                                "id": "3"
                            }
                        ]
                    },
                    {
                        "question": {
                            "whatStatistics": "Bodily accidents according to their nature 1991 - 2018 statistics for 2014 year:",
                            "whatValue": "Collision between a vehicle and a tree amount is {value}",
                            "value": 83,
                            "imgSrc": "https://source.unsplash.com/random?quiz&version=1",
                            "correctAnswerId": "2",
                            "url": "https://data.public.lu/fr/datasets/r/5c3e61cf-6384-487e-8451-03da2ede5d1c",
                            "answerUrl": "https://data.public.lu/fr/datasets/r/7acd5f82-4bd3-4315-b067-3504a078b47b"
                        },
                        "id": "1",
                        "answers": [
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "Complete wagons amount in 1970",
                                "id": "0"
                            },
                            {
                                "answerStatistics": "by Results of the exams for obtaining a driving license 1991 - 2018 statistics",
                                "answerValue": "> 45 years old amount in 2010",
                                "id": "1"
                            },
                            {
                                "answerStatistics": "by Road traffic injuries by month in 2018 statistics",
                                "answerValue": "Total victims killed amount in 1991",
                                "id": "2"
                            },
                            {
                                "answerStatistics": "by Rolling stock 1950 - 2018 statistics",
                                "answerValue": "including trailers amount in 2017",
                                "id": "3"
                            }
                        ]
                    },
                    {
                        "question": {
                            "whatStatistics": "Road traffic injuries by month in 2018 statistics for 2000 year:",
                            "whatValue": "Total victims killed amount is {value}",
                            "value": 76,
                            "imgSrc": "https://source.unsplash.com/random?quiz&version=2",
                            "correctAnswerId": "3",
                            "url": "https://data.public.lu/fr/datasets/r/7acd5f82-4bd3-4315-b067-3504a078b47b",
                            "answerUrl": "https://data.public.lu/fr/datasets/r/841f1af6-7e68-4f4a-96d8-a9bf76ee3267"
                        },
                        "id": "2",
                        "answers": [
                            {
                                "answerStatistics": "by Rolling stock 1950 - 2018 statistics",
                                "answerValue": "kW amount in 2010",
                                "id": "0"
                            },
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "Netherlands amount in 2013",
                                "id": "1"
                            },
                            {
                                "answerStatistics": "by Benelux product and service brands 1970 - 2018 statistics",
                                "answerValue": "Non residents amount in 2012",
                                "id": "2"
                            },
                            {
                                "answerStatistics": "by Bodily accidents and road traffic victims 1970 - 2018 statistics",
                                "answerValue": "You are amount in 2000",
                                "id": "3"
                            }
                        ]
                    },
                    {
                        "question": {
                            "whatStatistics": "Bodily accidents and road traffic victims 1970 - 2018 statistics for 2000 year:",
                            "whatValue": "You are amount is {value}",
                            "value": 76,
                            "imgSrc": "https://source.unsplash.com/random?quiz&version=3",
                            "correctAnswerId": "1",
                            "url": "https://data.public.lu/fr/datasets/r/bdce9238-32ea-4937-bd96-e720bdf78a2c",
                            "answerUrl": "https://data.public.lu/fr/datasets/r/7acd5f82-4bd3-4315-b067-3504a078b47b"
                        },
                        "id": "3",
                        "answers": [
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "Export amount in 2011",
                                "id": "0"
                            },
                            {
                                "answerStatistics": "by Interventions by Civil Protection ambulances 1962 - 2016 statistics",
                                "answerValue": "Interventions amount in 2015",
                                "id": "1"
                            },
                            {
                                "answerStatistics": "by Luxembourg patent applications filed, broken down according to the technical field to which the invention belongs 1980 - 2018 statistics",
                                "answerValue": "Total amount in 2000",
                                "id": "2"
                            },
                            {
                                "answerStatistics": "by Road traffic injuries by month in 2018 statistics",
                                "answerValue": "Total victims killed amount in 2000",
                                "id": "3"
                            }
                        ]
                    },
                    {
                        "question": {
                            "whatStatistics": "Road traffic injuries by month in 2018 statistics for 2010 year:",
                            "whatValue": "Total victims killed amount is {value}",
                            "value": 32,
                            "imgSrc": "https://source.unsplash.com/random?quiz&version=4",
                            "correctAnswerId": "3",
                            "url": "https://data.public.lu/fr/datasets/r/7acd5f82-4bd3-4315-b067-3504a078b47b",
                            "answerUrl": "https://data.public.lu/fr/datasets/r/7b457206-a8c4-4396-9a0e-84bc40ccef4d"
                        },
                        "id": "4",
                        "answers": [
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "Total amount in 2015",
                                "id": "0"
                            },
                            {
                                "answerStatistics": "by Freight traffic 1938 - 2018 statistics",
                                "answerValue": "1,000 tonne-kilometers amount in 2017",
                                "id": "1"
                            },
                            {
                                "answerStatistics": "by Road traffic injuries by month in 2018 statistics",
                                "answerValue": "Total victims killed amount in 2016",
                                "id": "2"
                            },
                            {
                                "answerStatistics": "by Length of the road network (in km) 1954 - 2019 statistics",
                                "answerValue": "State roads amount in 1990",
                                "id": "3"
                            }
                        ]
                    }
                ]
            }
        )
    except Exception as e:
        return json({"Error": "Sorry, cannot generate questions for you this time"})


@app.route("/")
async def welcome_view(request):
    return json({"message": "Welcome to lquiz-backend API"})


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))