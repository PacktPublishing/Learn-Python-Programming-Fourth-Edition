# railway-project/src/railway_cli/api/client.py
"""Client classes for interacting with the railway API."""

from typing import Any
from urllib.parse import urljoin

import requests

from ..exceptions import APIError
from .schemas import Station, StationList, Train, TrainList


class HTTPClient:
    """A client for making HTTP requests to the API."""

    def __init__(self, base_uri: str) -> None:
        """Initialize the client with a base URI."""
        self._base_uri = base_uri
        self._session = requests.Session()

    def get(self, path: str, **kwargs: Any) -> Any:
        """Make a GET request to the specified path."""
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Any:
        """Make a POST request to the specified path."""
        return self._request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Any:
        """Make a PUT request to the specified path."""
        return self._request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Any:
        """Make a DELETE request to the specified path."""
        return self._request("DELETE", path, **kwargs)

    def _request(
        self, method: str, path: str, **kwargs: Any
    ) -> Any:
        """Make an HTTP request to the specified path."""
        url = urljoin(self._base_uri, path)
        try:
            response = self._session.request(
                method, url, **kwargs
            )
        except requests.exceptions.RequestException as err:
            raise APIError(
                f"Error connecting to {url}: {err}"
            ) from err

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise APIError(
                _get_response_data(response) or str(err)
            ) from err
        else:
            return _get_response_data(response)


class StationClient:
    """A client for station-related endpoints."""

    path = "stations/"

    def __init__(self, api_client: HTTPClient) -> None:
        """Initialize the StationClient with an HTTPClient."""
        self._client = api_client

    def get(self, station_id: int) -> Station:
        """Get a station by its ID."""
        path = urljoin(self.path, str(station_id))
        data = self._client.get(path)
        return Station.model_validate(data)

    def find(self, code: str | None = None) -> list[Station]:
        """Find stations by code."""
        data = self._client.get(self.path, params={"code": code})
        stations = StationList.model_validate(data)
        return stations.root

    def get_arrivals(self, station_id: int) -> list[Train]:
        """Get arrivals for a station."""
        path = urljoin(self.path, f"{station_id}/arrivals")
        data = self._client.get(path)
        trains = TrainList.model_validate(data)
        return trains.root

    def get_departures(self, station_id: int) -> list[Train]:
        """Get departures for a station."""
        path = urljoin(self.path, f"{station_id}/departures")
        data = self._client.get(path)
        trains = TrainList.model_validate(data)
        return trains.root

    def create(
        self, code: str, country: str, city: str
    ) -> Station:
        """Create a new station."""
        response = self._client.post(
            self.path,
            json={"code": code, "country": country, "city": city},
        )
        return Station.model_validate(response)

    def update(self, station_id: int, **kwargs: str) -> None:
        """Update an existing station."""
        path = urljoin(self.path, str(station_id))
        self._client.put(path, json=kwargs)


class AdminClient:
    """A client for admin-related endpoints."""

    admin_path = "admin/"
    users_path = "users/"

    def __init__(self, api_client: HTTPClient) -> None:
        """Initialize the AdminClient with an HTTPClient."""
        self.auth_token: str | None = None
        self._client = api_client

    def authenticate(self, email: str, password: str) -> None:
        """Authenticate with the admin API."""
        path = urljoin(self.users_path, "authenticate")
        self.auth_token = self._client.post(
            path, json={"email": email, "password": password}
        )

    def delete_station(self, station_id: int) -> None:
        """Delete a station as an admin."""
        path = urljoin(self.admin_path, f"stations/{station_id}")
        self._client.delete(path, headers=self._auth_headers)

    @property
    def _auth_headers(self) -> dict[str, str]:
        """Get the authentication headers."""
        if not self.auth_token:
            raise APIError("Not authenticated")

        return {"Authorization": f"Bearer {self.auth_token}"}


def _get_response_data(response: requests.Response) -> Any:
    """Extract data from an HTTP response."""
    if response.status_code == 204:  # No Content
        return None

    try:
        return response.json()  # Attempt to parse JSON response
    except requests.exceptions.JSONDecodeError:
        return response.text  # Fall back to plain text response
