# pylint: disable=redefined-outer-name,unused-argument
import os

import pytest

from pyramid.router import Router


TEST_DIR = os.path.dirname(__file__)
INI_FILE = os.path.join(TEST_DIR, '..', 'config', 'testing.ini')


# -- shared fixtures

@pytest.fixture(scope='session')
def dotenv() -> None:
    from rapperswil_jona.env import Env

    if not os.environ.get('ENV', None):
        os.environ['ENV'] = 'test'

    # same as rapperswil_jona:main
    dotenv_file = os.path.join(os.getcwd(), '.env')
    Env.load_dotenv_vars(dotenv_file)


@pytest.fixture(scope='session')
def env(dotenv):
    from rapperswil_jona.env import Env

    return Env()


@pytest.fixture(scope='session')
def raw_settings(dotenv):
    from pyramid.paster import get_appsettings

    return get_appsettings('{0:s}#{1:s}'.format(INI_FILE, 'rapperswil_jona'))


@pytest.fixture(scope='session')
def resolve_settings():

    def _resolve_settings(raw_s):
        # pass
        return raw_s

    return _resolve_settings


@pytest.fixture(scope='session')
def settings(raw_settings, resolve_settings):
    return resolve_settings(raw_settings)


@pytest.fixture(scope='session')
def extra_environ(env):
    environ = {
        'SERVER_PORT': '80',
        'REMOTE_ADDR': '127.0.0.1',
        'wsgi.url_scheme': 'http',
    }
    return environ


# -- auto fixtures

@pytest.yield_fixture(autouse=True, scope='session')
def session_helper():
    yield


@pytest.yield_fixture(autouse=True, scope='module')
def module_helper(settings):
    yield


@pytest.yield_fixture(autouse=True, scope='function')
def function_helper():
    yield


# -- for unit tests

@pytest.fixture(scope='session')
def config(request, settings):
    from pyramid import testing

    config = testing.setUp(settings=settings)

    config.include('pyramid_assetviews')
    config.include('pyramid_chameleon')
    config.include('pyramid_secure_response')

    config.include('rapperswil_jona.route')
    config.include('rapperswil_jona.view')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)

    return config


@pytest.fixture(scope='function')
def dummy_request(extra_environ):
    from pyramid import testing

    locale_name = 'en'
    req = testing.DummyRequest(
        subdomain='',
        environ=extra_environ,
        _LOCALE_=locale_name,
        locale_name=locale_name,
        matched_route=None)

    return req


# -- for functional tests

@pytest.fixture(scope='session')
def router(raw_settings) -> Router:
    """Returns the internal app of app for testing."""
    from rapperswil_jona import main

    global_config = {
        '__file__': INI_FILE
    }
    if '__file__' in raw_settings:
        del raw_settings['__file__']

    return main(global_config, **raw_settings)


@pytest.fixture(scope='session')
def dummy_app(router, extra_environ):
    from webtest import TestApp

    return TestApp(router, extra_environ=extra_environ)
