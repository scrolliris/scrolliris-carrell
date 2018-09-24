import sys

from rapperswil_jona.env import Env


def main(argv=None, quiet=False):
    """Runs original pserve with .env support."""
    # NOTE:
    # `pserve` (PServeCommand) needs `hupper`, it has dependency to **fcntl**.
    # In some environment (e.g. app engine), fcntl is not found :'(
    # So, that's why this import is in method.
    from pyramid.scripts.pserve import PServeCommand

    if not argv:
        argv = sys.argv

    Env.load_dotenv_vars()

    command = PServeCommand(argv, quiet=quiet)
    return command.run()


if __name__ == '__main__':
    sys.exit(main(argv=None, quiet=False) or 0)
