# project/railway_cli/commands/__init__.py
import argparse

from .admin import admin_commands
from .base import Command
from .stations import station_commands


def configure_parsers(parser: argparse.ArgumentParser) -> None:
    """Configure the commandline argument parser.

    This adds a sub-parser for each command and configures it by
    calling the command's `configure_arg_parser` method. The
    command class is assigned to the `command` attribute of the
    parser. This allows the main function to access the command
    that was selected by the user.
    """
    subparsers = parser.add_subparsers(
        description="Available commands", required=True
    )

    command: type[Command]
    for command in [*admin_commands, *station_commands]:
        command_parser = subparsers.add_parser(
            command.name, help=command.help
        )
        command.configure_arg_parser(command_parser)
        command_parser.set_defaults(command=command)
