import os
import sys

from app.cli_dispatch import Dispatcher


class Command(object):
    """
    Docopt example with subcommands.

    Usage:
      docopt-example [options] [COMMAND] [ARGS...]
      docopt-example -h|--help

    Options:
      -v, --version                 Print version and exit

    Commands:
      subcommand_without_argument   Do something
      subcommand_with_argument      Do something else
    """

    def subcommand_without_argument(self):
        """
        List projects.

        Usage:
          subcommand_without_arguments
        """
        print('Executing subcommand_without_argument')

    def subcommand_with_argument(self):
        """
        Switch to a project

        Usage:
          subcommand_with_argument [THING]
        """
        print('Executing subcommand_with_argument')


def get_version_info():
    file = os.path.join(os.path.dirname(__file__), 'version.txt')
    return open(file).read().strip()


def main():
    dispatcher = Dispatcher(
        Command(),
        {'options_first': True, 'version': get_version_info()})

    options, handler, command_options = dispatcher.parse(sys.argv[1:])

    handler()
