# project/railway_cli/commands/admin.py
"""This module defines the commands for administrative tasks."""

import argparse
from typing import Any

from ..api.client import AdminClient
from ..config import get_admin_credentials
from .base import Command


class AdminCommand(Command):
    """Base class for administrative commands.

    Provides common functionality such as retrieving admin
    settings and authentication.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.credentials = get_admin_credentials(
            self.args, self.settings
        )
        self.admin_client = AdminClient(self.api_client)

    def authenticate(self) -> None:
        """Authenticate the admin client."""
        self.admin_client.authenticate(
            email=self.credentials.email,
            password=self.credentials.password.get_secret_value(),
        )


class DeleteStation(AdminCommand):
    """Command to delete a station."""

    name = "admin-delete-station"
    help = "Delete a station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        parser.add_argument(
            "station_id", type=int, help="The station ID"
        )

    def execute(self) -> None:
        """Execute the delete station command."""
        self.authenticate()
        self.admin_client.delete_station(self.args.station_id)


admin_commands = (DeleteStation,)
