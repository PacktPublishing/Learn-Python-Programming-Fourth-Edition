# railway-project/src/railway_cli/cli.py
"""This module sets up the command-line interface for the railway
CLI application.

It configures argument parsers and executes the appropriate
commands based on user input.
"""

import argparse
import sys
from importlib.metadata import metadata, packages_distributions

from . import __version__, commands, config, exceptions
from .commands.base import Command


def main(cmdline: list[str] | None = None) -> None:
    """The main entry point for the CLI application.

    Parses command-line arguments and executes the appropriate
    command.
    """
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args(cmdline)

    try:
        # args.command is expected to be a Command class
        command: Command = args.command(args)
        command.execute()
    except exceptions.APIError as exc:
        sys.exit(f"API error: {exc}")
    except exceptions.CommandError as exc:
        sys.exit(f"Command error: {exc}")
    except exceptions.ConfigurationError as exc:
        sys.exit(f"Configuration error: {exc}")


def get_arg_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Commandline interface for the Railway API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-L",
        "--license",
        action="version",
        version=get_license(),
    )
    config.configure_arg_parser(parser)
    commands.configure_parsers(parser)
    return parser


def get_license() -> str:
    """Return the license text."""
    default = "License not found"

    all_distributions = packages_distributions()
    try:
        distribution = all_distributions[__package__][0]
    except KeyError:
        return default

    meta = metadata(distribution)

    return meta["License"] or default
