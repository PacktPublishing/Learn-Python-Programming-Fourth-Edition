# api_code/api/database.py
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import Settings


settings = Settings()


DB_URL = "sqlite:///train.db"


engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
    echo=settings.debug,  # when debug is True, queries are logged
)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Ensure foreign key constraints are enforced in SQLite.

    By default, SQLite ignores foreign key constraints.
    To enforce foreign key constraints, we need to set the
    foreign_keys pragma to ON. This needs to be done for each
    database connection.

    We use an event listener to execute the pragma statement every
    time SQLAlchemy establishes a connection to the database.

    See https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
