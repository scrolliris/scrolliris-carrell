import sys
from wsgiref.handlers import BaseHandler

from pyramid.config import Configurator
from pyramid.threadlocal import get_current_registry
import better_exceptions

from rapperswil_jona.env import Env
import rapperswil_jona.logger  # noqa

better_exceptions.MAX_LENGTH = None


# -- util

# broken pipe error
def ignore_broken_pipes(self):
    # pylint: disable=protected-access
    if sys.version_info[0] > 2:
        # pylint: disable=undefined-variable
        if sys.exc_info()[0] != BrokenPipeError:  # noqa
            BaseHandler.__handle_error_original_(self)


# pylint: disable=protected-access
BaseHandler.__handle_error_original_ = BaseHandler.handle_error
BaseHandler.handle_error = ignore_broken_pipes
# pylint: enable=protected-access


def get_settings():
    """Returns settings from current ini."""
    return get_current_registry().settings


def resolve_env_vars(settings):
    env = Env()
    s = settings.copy()
    for k, v in Env.settings_mappings().items():
        # ignores missing key or it has a already value in config
        if k not in s or s[k]:
            continue
        new_v = env.get(v, None)
        if not isinstance(new_v, str):
            continue
        # ignores empty string
        if ',' in new_v:
            s[k] = [nv for nv in new_v.split(',') if nv != '']
        elif new_v:
            s[k] = new_v
    return s


# -- entry point

def main(_, **settings):
    from rapperswil_jona.request import CustomRequest

    config = Configurator(settings=resolve_env_vars(settings))

    config.include('.route')
    config.include('.view')

    config.set_request_factory(CustomRequest)

    config.scan()
    app = config.make_wsgi_app()

    # from rapperswil_jona.logger import enable_translogger
    # app = enable_translogger(app)
    return app
