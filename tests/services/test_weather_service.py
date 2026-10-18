import pytest

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather.models import Forecast
from weather.services.weather_service import WeatherService

VALID_API_KEY = "demo-key"


@pytest.fixture
def service() -> WeatherService:
    return WeatherService(api_key=VALID_API_KEY)


@pytest.mark.parametrize(
    "expected",
    [
        Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
        Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
    ],
)
def test_get_forecast_returns_forecast_for_known_city(
    service: WeatherService, expected: Forecast
) -> None:
    forecast = service.get_forecast(expected.city)

    assert forecast == expected


def test_unknown_city_raises_city_not_found(service: WeatherService) -> None:
    with pytest.raises(CityNotFoundError) as exc_info:
        service.get_forecast("Atlantis")

    assert exc_info.value.city == "Atlantis"


@pytest.mark.parametrize("api_key", ["wrong-key", "", "DEMO-KEY"])
def test_invalid_api_key_raises(api_key: str) -> None:
    service = WeatherService(api_key=api_key)

    with pytest.raises(InvalidAPIKeyError):
        service.get_forecast("Kigali")


def test_api_key_is_checked_before_the_city() -> None:
    service = WeatherService(api_key="wrong-key")

    with pytest.raises(InvalidAPIKeyError):
        service.get_forecast("Atlantis")


@pytest.mark.parametrize("city", ["kigali", "KIGALI", "  Kigali  ", "kiGALi"])
def test_city_name_ignores_case_and_surrounding_spaces(
    service: WeatherService, city: str
) -> None:
    forecast = service.get_forecast(city)

    assert forecast.city == "Kigali"


@pytest.mark.parametrize("city", ["", "   "])
def test_blank_city_raises_city_not_found(service: WeatherService, city: str) -> None:
    with pytest.raises(CityNotFoundError):
        service.get_forecast(city)
