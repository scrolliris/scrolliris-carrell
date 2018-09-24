from os import path

from rapperswil_jona.env import Env

STATIC_DIR = path.join(path.dirname(path.abspath(__file__)), '../static')


def includeme(config):
    env = Env()
    cache_max_age = 3600 if env.is_production else 0

    # routes
    # static files at /*
    filenames = [f for f in ('robots.txt', 'humans.txt', 'favicon.ico')
                 if path.isfile((STATIC_DIR + '/{}').format(f))]
    if filenames:
        config.add_asset_views(
            STATIC_DIR, filenames=filenames, http_cache=cache_max_age)

    # static files at /assets/*
    config.add_static_view(
        name='assets', path=STATIC_DIR, cache_max_age=cache_max_age)

    config.add_route('index', '/')
