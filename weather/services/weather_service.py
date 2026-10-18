"""Weather service that returns forecasts for cities."""

import logging

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather.models import Forecast
from weather.utils.formatters import normalize_city_name

_KNOWN_FORECASTS = (
    Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
    Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
)

_FORECASTS_BY_CITY = {
    normalize_city_name(forecast.city): forecast for forecast in _KNOWN_FORECASTS
}
_VALID_API_KEYS = frozenset({"demo-key"})

logger = logging.getLogger(__name__)


class WeatherService:
    """Provides weather forecasts for cities."""

    def __init__(self, api_key: str) -> None:
        """Create the service with the API key used for every request.

        Args:
            api_key: The key that identifies the caller.
        """
        self._api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city.

        Returns:
            The forecast for the city.

        Raises:
            CityNotFoundError: if there is no forecast for the city.
            InvalidAPIKeyError: If the service's API key is not valid.
        """
        logger.info("forecast requested city=%s", city)
        if self._api_key not in _VALID_API_KEYS:
            logger.warning("request rejected reason=invalid_api_key")
            raise InvalidAPIKeyError()
        forecast = _FORECASTS_BY_CITY.get(normalize_city_name(city))
        if forecast is None:
            logger.warning("city not found city=%s", city)
            raise CityNotFoundError(city)
        logger.info(
            "forecast returned city=%s condition=%s", forecast.city, forecast.condition
        )
        return forecast
