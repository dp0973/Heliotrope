import os
from _pytest.config import Config
from sanic.app import Sanic

from tests.case import galleyinfo, info
from pytest import fixture
from tortoise import Tortoise, run_async
from heliotrope.database.mongo import NoSQLQuery
from heliotrope.database.query import SQLQuery
from sanic_testing import TestManager  # type:ignore
from heliotrope.server import heliotrope


# def pytest_configure(config: Config):
#     async def query():
#         mongo = NoSQLQuery(os.environ["MONGODB_URL"])
#         await Tortoise.init(
#             db_url=os.environ["DB_URL"],
#             modules={
#                 "models": [
#                     "heliotrope.database.models.hitomi",
#                     "heliotrope.database.models.requestcount",
#                 ]
#             },
#         )
#         await Tortoise.generate_schemas()
#         orm = SQLQuery()
#         await orm.add_galleryinfo(galleyinfo)
#         await mongo.insert_info(info)

#     run_async(query())


@fixture()
def app() -> Sanic:
    TestManager(heliotrope)
    return heliotrope
