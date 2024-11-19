# railway-project/src/railway_cli/exceptions.py
"""Exceptions for the railway CLI."""


class RailwayCLIError(Exception):
    """Base class for railway CLI exceptions."""


class APIError(RailwayCLIError):
    """An exception for errors coming from the API."""


class CommandError(RailwayCLIError):
    """An exception for errors in the CLI commands."""


class ConfigurationError(RailwayCLIError):
    """An exception for configuration errors."""
