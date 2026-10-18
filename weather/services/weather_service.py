"""Weather service that returns forecasts for cities."""

from weather.exceptions import CityNotFoundError
from weather.models import Forecast

_KNOWN_FORECASTS = (
    Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
    Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
)

_FORECASTS_BY_CITY = {forecast.city: forecast for forecast in _KNOWN_FORECASTS}


class WeatherService:
    """Provides weather forecasts for cities."""

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: Name of the city.

        Returns:
            The forecast for the city.

        Raises:
            CityNotFoundError: if there is no forecast for the city.
        """
        forecast = _FORECASTS_BY_CITY.get(city)
        if forecast is None:
            raise CityNotFoundError(city)
        return forecast
