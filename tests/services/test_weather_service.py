import pytest

from weather.exceptions import CityNotFoundError
from weather.models import Forecast
from weather.services.weather_service import WeatherService


@pytest.mark.parametrize(
    "expected",
    [
        Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
        Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
    ],
)
def test_get_forecast_returns_forecast_for_known_city(expected: Forecast) -> None:
    service = WeatherService()

    forecast = service.get_forecast(expected.city)

    assert forecast == expected


def test_unknown_city_raises_city_not_found() -> None:
    service = WeatherService()

    with pytest.raises(CityNotFoundError) as exc_info:
        service.get_forecast("Atlantis")

    assert exc_info.value.city == "Atlantis"
