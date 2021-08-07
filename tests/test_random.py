from sanic_testing.manager import TestManager  # type:ignore

url = "/v5/api/hitomi/random"


def test_random(app: TestManager):
    _, response = app.test_client.get()
    assert response.status == 200
