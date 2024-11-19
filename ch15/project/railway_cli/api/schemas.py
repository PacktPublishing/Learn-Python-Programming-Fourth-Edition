# project/railway_cli/api/schemas.py
"""Pydantic schemas for objects received from the API."""

from datetime import datetime

from pydantic import BaseModel, RootModel


class Station(BaseModel):
    """A class to represent a station.

    This should match the API response schema for a station
    """

    id: int
    code: str
    country: str
    city: str


StationList = RootModel[list[Station]]


class Train(BaseModel):
    """A class to represent a train.

    This should match the API response schema for a train
    """

    id: int
    name: str
    station_from: Station
    station_to: Station
    departs_at: datetime
    arrives_at: datetime
    first_class: int
    second_class: int
    seats_per_car: int


TrainList = RootModel[list[Train]]
