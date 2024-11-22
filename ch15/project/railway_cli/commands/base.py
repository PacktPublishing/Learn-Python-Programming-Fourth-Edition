# project/railway_cli/commands/base.py
"""This module defines a base class for commands."""

import argparse
from typing import ClassVar

from ..api.client import HTTPClient
from ..config import get_settings


class Command:
    """A base class to represent a command."""

    name: ClassVar[str]
    help: ClassVar[str]

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.settings = get_settings(args)
        self.api_client = HTTPClient(self.settings.url)

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the parser for this command."""
        raise NotImplementedError

    def execute(self) -> None:
        """Execute this command."""
        raise NotImplementedError
