"""Weather service that returns forecasts for cities."""

import logging

from weather.models import Forecast
from weather.providers.mock_weather_provider import MockWeatherProvider

logger = logging.getLogger(__name__)


class WeatherService:
    """Provides weather forecasts for cities.

    The forecasts come from a mock provider that simulates a weather
    API, so results are always predictable.
    """

    def __init__(self, api_key: str) -> None:
        """Create the service with the API key used for every request.

        Args:
            api_key: The key that identifies the caller.
        """
        self._provider = MockWeatherProvider(api_key)

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city, for example "Kigali".

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
            CityNotFoundError: If there is no forecast for the city.
        """
        logger.info("forecast requested city=%s", city)
        forecast = self._provider.get_forecast(city)
        logger.info(
            "forecast returned city=%s condition=%s", forecast.city, forecast.condition
        )
        return forecast
