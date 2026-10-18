"""Abstract interface for sources of weather forecasts."""

from abc import ABC, abstractmethod

from weather.models import Forecast


class WeatherProvider(ABC):
    """A source of weather forecasts, such as an external weather API.

    The service depends only on this interface, so a mock provider can
    be swapped for one that calls a real API without changing the
    service.
    """

    @abstractmethod
    def get_forecast(self, city: str) -> Forecast:
        """Fetch the forecast for a city.

        Args:
            city: Name of the city.

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the provider rejects the API key.
            CityNotFoundError: If the provider has no forecast for the city.
        """
