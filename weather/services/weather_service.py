"""Weather service that returns forecasts for cities."""

from weather.models import Forecast

_FORECASTS = {
    "Kigali": Forecast(
        city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"
    ),
    "Nairobi": Forecast(
        city="Nairobi", temperature_celsius=22.0, condition="Light rain"
    ),
}


class WeatherService:
    """Provides weather forecasts for cities."""

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city.

        Returns:
            The forecast for the city.
        """
        return _FORECASTS[city]
