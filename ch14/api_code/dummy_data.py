# api_code/dummy_data.py
from datetime import UTC, datetime, timedelta
from pathlib import Path
from random import choice, randint, random, sample

from api.models import (
    Base,
    Classes,
    Roles,
    Station,
    Ticket,
    Train,
    User,
)
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DB_URL = "sqlite:///train.db"
engine = create_engine(DB_URL, echo=True)

HOUR = 60 * 60
DAY = 24 * HOUR
TEN_DAYS = 10 * DAY
YEAR = 365 * DAY
TEN_YEARS = 10 * YEAR
NOW = datetime.now(UTC)


def new_db(filename: str) -> None:
    print("Creating a new database...")

    db_file = Path(filename)
    db_file.unlink(missing_ok=True)

    # then create a fresh DB
    Base.metadata.create_all(engine)


def get_users(fake: Faker, num_users: int) -> list[User]:
    return [
        User(
            id=0,
            full_name="Fabrizio Romano",
            email="fabrizio.romano@example.com",
            password=User.hash_password("f4bPassword"),
            role=Roles.admin,
        ),
        *(
            User(
                id=user_id,
                full_name=fake.name(),
                email=fake.safe_email(),
                password=User.hash_password(fake.password()),
                role=Roles.passenger,
            )
            for user_id in range(1, num_users)
        ),
    ]


def get_stations() -> list[Station]:
    return [
        Station(id=0, code="ROM", country="Italy", city="Rome"),
        Station(id=1, code="PAR", country="France", city="Paris"),
        Station(id=2, code="LDN", country="UK", city="London"),
        Station(id=3, code="KYV", country="Ukraine", city="Kyiv"),
        Station(
            id=4,
            code="STK",
            country="Sweden",
            city="Stockholm",
        ),
        Station(
            id=5, code="WSW", country="Poland", city="Warsaw"
        ),
        Station(
            id=6, code="MSK", country="Russia", city="Moskow"
        ),
        Station(
            id=7,
            code="AMD",
            country="Netherlands",
            city="Amsterdam",
        ),
        Station(
            id=8,
            code="EDB",
            country="Scotland",
            city="Edinburgh",
        ),
        Station(
            id=9,
            code="BDP",
            country="Hungary",
            city="Budapest",
        ),
        Station(
            id=10,
            code="BCR",
            country="Romania",
            city="Bucharest",
        ),
        Station(
            id=11,
            code="SFA",
            country="Bulgaria",
            city="Sofia",
        ),
    ]


def get_trains(
    stations: list[Station], num_trains: int
) -> list[Train]:
    return [
        get_train(train_id, stations)
        for train_id in range(num_trains)
    ]


def get_train(train_id: int, stations: list[Station]) -> Train:
    station_from, station_to = sample(stations, k=2)

    name = f"{station_from.city} -> {station_to.city}"
    departure = NOW + timedelta(
        seconds=randint(-YEAR, TEN_YEARS)
    )
    arrival = departure + timedelta(seconds=randint(HOUR, DAY))

    return Train(
        id=train_id,
        name=name,
        station_from=station_from,
        station_to=station_to,
        departs_at=departure,
        arrives_at=arrival,
        first_class=randint(0, 3),
        second_class=randint(3, 10),
        seats_per_car=choice([10, 25, 40]),
    )


def get_tickets(
    users: list[User],
    trains: list[Train],
    num_tickets: int,
    min_price: float | int,
    max_price: float | int,
) -> list[Ticket]:
    return [
        get_ticket(ticket_id, users, trains, min_price, max_price)
        for ticket_id in range(num_tickets)
    ]


def get_ticket(
    ticket_id: int,
    users: list[User],
    trains: list[Train],
    min_price: float | int,
    max_price: float | int,
) -> Ticket:
    created_at = NOW + timedelta(
        seconds=randint(-TEN_DAYS, -HOUR)
    )
    price = round(
        (max_price - min_price) * random() + min_price,
        randint(0, 2),
    )
    return Ticket(
        id=ticket_id,
        created_at=created_at,
        user=choice(users),
        train=choice(trains),
        price=price,
        car_class=choice(list(Classes)),
    )


if __name__ == "__main__":
    new_db("train.db")

    with Session(engine) as session, session.begin():

        fake = Faker()

        NUM_USERS = 100
        NUM_TICKETS = 500
        NUM_TRAINS = 500
        MIN_PRICE = 5
        MAX_PRICE = 200

        # USERS

        print("Creating users...")
        users = get_users(fake, NUM_USERS)
        session.add_all(users)

        # STATIONS

        print("Creating stations...")
        stations = get_stations()
        session.add_all(stations)

        # TRAINS

        print("Creating trains...")
        trains = get_trains(stations, NUM_TRAINS)
        session.add_all(trains)

        # TICKETS

        print("Creating tickets...")
        tickets = get_tickets(
            users=users[:-1],  # last user has no tickets
            trains=trains[:-1],  # last train has no tickets
            num_tickets=NUM_TICKETS,
            min_price=MIN_PRICE,
            max_price=MAX_PRICE,
        )
        session.add_all(tickets)

    print("done")
