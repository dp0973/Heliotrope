from sanic_testing.manager import TestManager  # type:ignore

url = "/v5/api/hitomi/random"


def test_random(app: TestManager):
    _, response = app.test_client.get(url)
    assert response.status == 200


def test_random_not_found(app: TestManager):
    _, response = app.test_client.get(url + "0")
    assert response.status == 404
