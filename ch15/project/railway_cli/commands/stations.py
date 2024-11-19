# project/railway_cli/commands/stations.py
"""This module defines the commands for managing railway stations.

It includes commands to get, list, create, update stations, and
retrieve arrivals and departures.
"""

import argparse
from functools import cached_property

from ..api.client import StationClient
from ..api.schemas import Station
from ..exceptions import CommandError
from .base import Command


class GetStation(Command):
    """Command to get details of a specific station."""

    name = "get-station"
    help = "Get a station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        id_code_group = parser.add_mutually_exclusive_group(
            required=True
        )
        id_code_group.add_argument(
            "--station-id",
            type=int,
            help="The station ID",
            default=argparse.SUPPRESS,
        )
        id_code_group.add_argument(
            "--station-code",
            help="The station code",
            default=argparse.SUPPRESS,
        )

    @cached_property
    def station_client(self) -> StationClient:
        """Create an instance of the StationClient."""
        return StationClient(self.api_client)

    def execute(self) -> None:
        """Execute the get station command."""
        match self.args:
            case argparse.Namespace(station_id=station_id):
                station = self.get_by_id(station_id)
            case argparse.Namespace(station_code=station_code):
                station = self.get_by_code(station_code)

        print(station)

    def get_by_id(self, station_id: int) -> Station:
        """Retrieve a station by its ID."""
        return self.station_client.get(station_id)

    def get_by_code(self, station_code: str) -> Station:
        """Retrieve a station by its code."""
        stations = self.station_client.find(code=station_code)

        if not stations:
            raise CommandError(
                f"Station with code {station_code} not found."
            )

        return stations[0]


class ListStations(Command):
    """Command to list all stations."""

    name = "list-stations"
    help = "List stations"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """This command takes no arguments."""

    def execute(self) -> None:
        """Execute the list stations command."""
        station_client = StationClient(self.api_client)
        stations = station_client.find()

        for station in stations:
            print(station)


class CreateStation(Command):
    """Command to create a new station."""

    name = "create-station"
    help = "Create a station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        parser.add_argument(
            "--code", help="The station code", required=True
        )
        parser.add_argument(
            "--country", help="The station country", required=True
        )
        parser.add_argument(
            "--city", help="The station city", required=True
        )

    def execute(self) -> None:
        """Execute the create station command."""
        station_client = StationClient(self.api_client)
        station = station_client.create(
            code=self.args.code,
            country=self.args.country,
            city=self.args.city,
        )

        print(station)


class UpdateStation(Command):
    """Command to update an existing station."""

    name = "update-station"
    help = "Update an existing station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        parser.add_argument(
            "--station-id", help="The station ID", required=True
        )
        parser.add_argument(
            "--code",
            help="The new station code",
            default=argparse.SUPPRESS,
        )
        parser.add_argument(
            "--country",
            help="The new station country",
            default=argparse.SUPPRESS,
        )
        parser.add_argument(
            "--city",
            help="The new station city",
            default=argparse.SUPPRESS,
        )

    def execute(self) -> None:
        """Execute the update station command."""
        station_client = StationClient(self.api_client)
        update_data = {
            key: value
            for key, value in vars(self.args).items()
            if key in {"station_id", "code", "country", "city"}
        }
        station_client.update(**update_data)


class GetArrivals(Command):
    """Command to get arrivals for a specific station."""

    name = "get-arrivals"
    help = "Get arrivals for a station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        parser.add_argument(
            "station_id", type=int, help="The station ID"
        )

    def execute(self) -> None:
        """Execute the get arrivals command."""
        station_client = StationClient(self.api_client)
        trains = station_client.get_arrivals(self.args.station_id)

        for train in trains:
            print(train)


class GetDepartures(Command):
    """Command to get departures for a specific station."""

    name = "get-departures"
    help = "Get departures for a station"

    @classmethod
    def configure_arg_parser(
        cls, parser: argparse.ArgumentParser
    ) -> None:
        """Configure the argument parser."""
        parser.add_argument(
            "station_id", type=int, help="The station ID"
        )

    def execute(self) -> None:
        """Execute the get departures command."""
        station_client = StationClient(self.api_client)
        trains = station_client.get_departures(
            self.args.station_id
        )

        for train in trains:
            print(train)


station_commands = (
    GetStation,
    ListStations,
    CreateStation,
    UpdateStation,
    GetArrivals,
    GetDepartures,
)
