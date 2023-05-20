"""
Environment requirements:

    Flask:
        DEBUG
            type: int | None
            default: 0
            description:
                0 - False
                1 - True
"""

from os import environ, getenv

__all__ = ['Config']


class Config:
    DEBUG_MODE = bool(int(getenv("DEBUG", 0)))

    SQLALCHEMY_DATABASE_URI = environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
