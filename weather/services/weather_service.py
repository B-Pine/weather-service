"""Weather service that returns forecasts for cities."""

from weather.models import Forecast


class WeatherService:
    """Provides weather forecasts for cities."""

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city.

        Returns:
            The forecast for the city.
        """
        raise NotImplementedError
