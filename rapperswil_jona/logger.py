import logging

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(sh)
# pylint: enable=invalid-name


# -- logger utils

def enable_translogger(app):
    """Makes `wsgi` logger which uses `access_log` handler enable.

    Same as to add `translogger` into [pipeline:main] section.
    """
    # pylint: disable=relative-import
    from paste.translogger import TransLogger
    return TransLogger(app, setup_console_handler=False)
