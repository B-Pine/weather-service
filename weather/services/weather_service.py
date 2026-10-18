"""Weather service that returns forecasts for cities."""

import logging

from weather.models import Forecast
from weather.providers.weather_provider import WeatherProvider

logger = logging.getLogger(__name__)


class WeatherService:
    """Provides weather forecasts for cities, and logs every request.

    The service gets its data from a provider passed in when it is
    created. It depends only on the WeatherProvider interface, so the
    mock provider can be replaced by a real API without changing it.
    """

    def __init__(self, provider: WeatherProvider) -> None:
        """Create the service with the provider it gets forecasts from.

        Args:
            provider: The source of forecasts.
        """
        self._provider = provider

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city, for example "Kigali".

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the provider rejects the API key.
            CityNotFoundError: If the provider has no forecast for the city.
        """
        logger.info("forecast requested city=%s", city)
        forecast = self._provider.get_forecast(city)
        logger.info(
            "forecast returned city=%s condition=%s", forecast.city, forecast.condition
        )
        return forecast
