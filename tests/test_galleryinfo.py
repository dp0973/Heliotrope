from sanic_testing.manager import TestManager  # type:ignore

url = "/v5/api/hitomi/galleryinfo/"


def test_galleryinfo(app: TestManager):
    _, response = app.test_client.get(url + "1570712")
    assert response.status == 200


def test_galleryinfo_not_found(app: TestManager):
    _, response = app.test_client.get(url + "0")
    assert response.status == 404
