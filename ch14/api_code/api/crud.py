# api_code/api/crud.py
from datetime import UTC, datetime

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session, aliased

from . import models, schemas


# USERS


def get_users(db: Session, email: str | None = None):
    stm = select(models.User)
    if email is not None:
        stm = stm.where(models.User.email.ilike(f"%{email}%"))
    return db.scalars(stm).all()


def get_user(db: Session, user_id: int):
    return db.scalar(
        select(models.User).where(models.User.id == user_id)
    )


def get_user_by_email(db: Session, email: str):
    return db.scalar(
        select(models.User).where(models.User.email.ilike(email))
    )


def create_user(
    db: Session, user: schemas.UserCreate, user_id: int = None
):
    hashed_password = models.User.hash_password(user.password)
    user_dict = {
        **user.model_dump(exclude_unset=True),
        "password": hashed_password,
    }
    if user_id is not None:
        user_dict.update({"id": user_id})
    db_user = models.User(**user_dict)
    db.add(db_user)
    db.commit()
    return db_user


def update_user(
    db: Session, user: schemas.UserUpdate, user_id: int
):
    user_dict = {
        **user.model_dump(exclude_unset=True),
    }
    if user.password is not None:
        user_dict.update(
            {"password": models.User.hash_password(user.password)}
        )
    stm = (
        update(models.User)
        .where(models.User.id == user_id)
        .values(user_dict)
    )
    result = db.execute(stm)
    db.commit()
    return result.rowcount


def delete_user(db: Session, user_id: int):
    stm = delete(models.User).where(models.User.id == user_id)
    result = db.execute(stm)
    db.commit()
    return result.rowcount


# STATIONS


def get_stations(db: Session, code: str | None = None):
    stm = select(models.Station)
    if code is not None:
        stm = stm.where(models.Station.code.ilike(code))
    return db.scalars(stm).all()


def get_station(db: Session, station_id: int):
    return db.scalar(
        select(models.Station).where(
            models.Station.id == station_id
        )
    )


def get_station_by_code(db: Session, code: str):
    return db.scalar(
        select(models.Station).where(
            models.Station.code.ilike(code)
        )
    )


def create_station(
    db: Session,
    station: schemas.StationCreate,
):
    db_station = models.Station(**station.model_dump())
    db.add(db_station)
    db.commit()
    return db_station


def update_station(
    db: Session, station: schemas.StationUpdate, station_id: int
):
    stm = (
        update(models.Station)
        .where(models.Station.id == station_id)
        .values(station.model_dump(exclude_unset=True))
    )
    result = db.execute(stm)
    db.commit()
    return result.rowcount


def delete_station(db: Session, station_id: int):
    stm = delete(models.Station).where(
        models.Station.id == station_id
    )
    result = db.execute(stm)
    db.commit()
    return result.rowcount


# TRAINS


def get_trains(
    db: Session,
    station_from_code: str = None,
    station_to_code: str = None,
    include_all: bool = False,
):
    stm = select(models.Train)

    if station_from_code is not None:
        st_from = aliased(models.Station)
        stm = stm.join(st_from, models.Train.station_from)
        stm = stm.where(
            st_from.code.ilike(f"%{station_from_code}%")
        )

    if station_to_code is not None:
        st_to = aliased(models.Station)
        stm = stm.join(st_to, models.Train.station_to)
        stm = stm.where(st_to.code.ilike(f"%{station_to_code}%"))

    if not include_all:
        now = datetime.now(UTC)
        stm = stm.where(models.Train.departs_at > now)

    return db.scalars(stm).all()


def get_train(db: Session, train_id: int):
    return db.scalar(
        select(models.Train).where(models.Train.id == train_id)
    )


def get_train_by_name(db: Session, name: str):
    return db.scalar(
        select(models.Train).where(models.Train.name == name)
    )


def create_train(db: Session, train: schemas.TrainCreate):
    train_dict = train.model_dump(exclude_unset=True)
    db_train = models.Train(**train_dict)
    db.add(db_train)
    db.commit()
    return db_train


def delete_train(db: Session, train_id: int):
    stm = delete(models.Train).where(models.Train.id == train_id)
    result = db.execute(stm)
    db.commit()
    return result.rowcount


# TICKETS


def get_tickets(db: Session):
    return db.scalars(select(models.Ticket)).all()


def get_ticket(db: Session, ticket_id: int):
    return db.scalar(
        select(models.Ticket).where(models.Ticket.id == ticket_id)
    )


def create_ticket(db: Session, ticket: schemas.TicketCreate):
    ticket_dict = ticket.model_dump(exclude_unset=True)
    ticket_dict.update({"created_at": datetime.now(UTC)})
    db_ticket = models.Ticket(**ticket_dict)
    db.add(db_ticket)
    db.commit()
    return db_ticket


def delete_ticket(db: Session, ticket_id: int):
    stm = delete(models.Ticket).where(
        models.Ticket.id == ticket_id
    )
    result = db.execute(stm)
    db.commit()
    return result.rowcount
