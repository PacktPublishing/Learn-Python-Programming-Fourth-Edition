# api_code/api/deps.py
from functools import lru_cache

from .config import Settings
from .database import SessionLocal


def get_db():
    """Return a DB Session."""
    with SessionLocal() as db:
        yield db


@lru_cache
def get_settings():
    """Return the app settings."""
    return Settings()
