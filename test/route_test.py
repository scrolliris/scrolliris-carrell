import pytest


@pytest.fixture(autouse=True)
def setup(request, config):  # pylint: disable=unused-argument
    def teardown():
        pass

    request.addfinalizer(teardown)


def test_routing_to_favicon(dummy_app):
    res = dummy_app.get('/favicon.ico', status=200)
    assert 200 == res.status_code


def test_routing_to_humans(dummy_app):
    res = dummy_app.get('/humans.txt', status=200)
    assert 200 == res.status_code


def test_routing_to_robots(dummy_app):
    res = dummy_app.get('/robots.txt', status=200)
    assert 200 == res.status_code
