"""Mock weather provider that simulates an external weather API."""

import logging

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather.models import Forecast
from weather.providers.weather_provider import WeatherProvider
from weather.utils.formatters import normalize_city_name

_KNOWN_FORECASTS = (
    Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
    Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
    Forecast(city="Kampala", temperature_celsius=26.0, condition="Thunderstorms"),
    Forecast(city="Dar es Salaam", temperature_celsius=30.0, condition="Sunny"),
)
_FORECASTS_BY_CITY = {
    normalize_city_name(forecast.city): forecast for forecast in _KNOWN_FORECASTS
}
_VALID_API_KEYS = frozenset({"demo-key"})

logger = logging.getLogger(__name__)


class MockWeatherProvider(WeatherProvider):
    """Simulates a weather API that returns predefined forecasts.

    Like a real API, it rejects requests with an invalid API key before
    looking anything up. Its results are always the same, which makes
    it predictable in tests and demos.
    """

    def __init__(self, api_key: str) -> None:
        """Create the provider with the API key sent with every request.

        Args:
            api_key: The key that identifies the caller.
        """
        self._api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Return the predefined forecast for a city.

        Args:
            city: Name of the city, in any letter case.

        Returns:
            The predefined forecast for the city.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
            CityNotFoundError: If there is no forecast for the city.
        """
        self._check_api_key()
        return self._find_forecast(city)

    def _check_api_key(self) -> None:
        """Reject the request if the API key is not valid.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
        """
        if self._api_key not in _VALID_API_KEYS:
            logger.warning("request rejected reason=invalid_api_key")
            raise InvalidAPIKeyError()

    def _find_forecast(self, city: str) -> Forecast:
        """Look up the predefined forecast for a city.

        Args:
            city: Name of the city, in any letter case.

        Returns:
            The forecast for the city.

        Raises:
            CityNotFoundError: If there is no forecast for the city.
        """
        forecast = _FORECASTS_BY_CITY.get(normalize_city_name(city))
        if forecast is None:
            logger.warning("city not found city=%s", city)
            raise CityNotFoundError(city)
        return forecast
