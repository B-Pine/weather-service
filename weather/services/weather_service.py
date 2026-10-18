"""Weather service that returns forecasts for cities."""

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather.models import Forecast

_KNOWN_FORECASTS = (
    Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
    Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
)

_FORECASTS_BY_CITY = {forecast.city: forecast for forecast in _KNOWN_FORECASTS}
_VALID_API_KEYS = frozenset({"demo-key"})
print(_VALID_API_KEYS)


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
        if self._api_key not in _VALID_API_KEYS:
            raise InvalidAPIKeyError()

        forecast = _FORECASTS_BY_CITY.get(city)
        if forecast is None:
            raise CityNotFoundError(city)
        return forecast
