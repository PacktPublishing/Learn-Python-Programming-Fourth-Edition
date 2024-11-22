# railway-project/test/test_get_station.py
from typing import Generator
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture
from requests_mock import Mocker as RequestsMocker

from railway_cli.config import Settings
from railway_cli.api.schemas import Station
from railway_cli.cli import main


@pytest.fixture
def requests_mock() -> Generator[RequestsMocker, None, None]:
    with RequestsMocker() as mock:
        yield mock


@pytest.fixture
def settings() -> Settings:
    return Settings(url="http://railway-api.test")


@pytest.fixture(autouse=True)
def mock_get_settings(
    mocker: MockerFixture, settings: Settings
) -> MagicMock:
    return mocker.patch(
        "railway_cli.commands.base.get_settings",
        return_value=settings,
    )


def test_mutually_exclusive_options() -> None:
    with pytest.raises(SystemExit):
        main(
            [
                "get-station",
                "--station-code",
                "TST",
                "--station-id",
                "42",
            ]
        )


def test_option_required() -> None:
    with pytest.raises(SystemExit):
        main([])


@pytest.fixture
def station() -> Station:
    return Station(
        id=42,
        code="TST",
        city="Testville",
        country="Testland",
    )


def test_get_by_id(
    station: Station,
    requests_mock: RequestsMocker,
    capsys: pytest.CaptureFixture[str],
) -> None:
    requests_mock.get(
        "http://railway-api.test/stations/42",
        json=station.model_dump(),
    )

    main(["get-station", "--station-id", "42"])

    assert capsys.readouterr().out == f"{station}\n"


def test_get_by_code(
    station: Station,
    requests_mock: RequestsMocker,
    capsys: pytest.CaptureFixture[str],
) -> None:
    requests_mock.get(
        "http://railway-api.test/stations/?code=TST",
        json=[station.model_dump()],
    )

    main(["get-station", "--station-code", "TST"])

    assert capsys.readouterr().out == f"{station}\n"


def test_station_code_not_found(
    requests_mock: RequestsMocker,
) -> None:
    requests_mock.get(
        "http://railway-api.test/stations/?code=TST",
        json=[],
    )

    with pytest.raises(SystemExit) as error:
        main(["get-station", "--station-code", "TST"])

    error.match("Station with code TST not found.")
