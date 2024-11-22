# api_code/api/schemas.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from . import models


# USERS


class Auth(BaseModel):
    email: str
    password: str


class AuthToken(BaseModel):
    token: str


class UserBase(BaseModel):
    full_name: str
    email: str
    role: models.Roles


class User(UserBase):
    model_config = ConfigDict(
        from_attributes=True, use_enum_values=True
    )
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    full_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[models.Roles] = None


# STATIONS


class StationBase(BaseModel):
    code: str
    country: str
    city: str


class Station(StationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class StationCreate(StationBase):
    pass


class StationUpdate(StationBase):
    code: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None


# TRAINS


class TrainBase(BaseModel):
    name: str
    station_from: Optional[Station] = None
    station_to: Optional[Station] = None
    departs_at: datetime
    arrives_at: datetime
    first_class: int
    second_class: int
    seats_per_car: int


class Train(TrainBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TrainCreate(TrainBase):
    station_from_id: int
    station_to_id: int


# TICKETS


class TicketBase(BaseModel):
    user_id: int
    train_id: int
    price: float
    car_class: models.Classes


class Ticket(TicketBase):
    model_config = ConfigDict(
        from_attributes=True, use_enum_values=True
    )
    id: int
    created_at: datetime


class TicketCreate(TicketBase):
    pass
