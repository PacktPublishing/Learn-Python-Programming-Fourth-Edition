# project/railway_cli/config.py
"""Configuration settings for the railway CLI."""

import argparse
from getpass import getpass

from pydantic import EmailStr, Field, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from .exceptions import ConfigurationError


class Settings(BaseSettings):
    """General settings for the railway CLI."""

    url: str
    secrets_dir: str | None = None


class AdminCredentials(BaseSettings):
    """Admin credentials for the railway CLI."""

    model_config = SettingsConfigDict(env_prefix="railway_api_")

    email: EmailStr
    password: SecretStr = Field(
        default_factory=lambda: SecretStr(
            getpass(prompt="Admin Password: ")
        )
    )


def configure_arg_parser(parser: argparse.ArgumentParser) -> None:
    """Configure global commandline arguments.

    This function sets up commandline arguments for specifying the
    configuration file and the secrets directory.
    """

    config_group = parser.add_argument_group(
        "configuration",
        description="""The API URL must be set in the
        configuration file. The admin email and password should be
        configured via secrets files named email and password in a
        secrets directory.""",
    )
    config_group.add_argument(
        "--config-file",
        help="Load configuration from a file",
        default=".env",
    )
    config_group.add_argument(
        "--secrets-dir",
        help="""The secrets directory. Can also be set via the
        configuration file.""",
    )


def get_settings(args: argparse.Namespace) -> Settings:
    """Retrieve general settings using the configuration file
    specified on the commandline."""
    try:
        return Settings(_env_file=args.config_file)
    except ValidationError as exc:
        raise ConfigurationError(str(exc)) from exc


def get_admin_credentials(
    args: argparse.Namespace, settings: Settings
) -> AdminCredentials:
    """Retrieve admin credentials using the secrets directory
    specified on the commandline or config file."""
    secrets_dir = args.secrets_dir
    if secrets_dir is None:
        secrets_dir = settings.secrets_dir

    try:
        return AdminCredentials(_secrets_dir=secrets_dir)
    except ValidationError as exc:
        raise ConfigurationError(str(exc)) from exc
