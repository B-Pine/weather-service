import logging

import pytest

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather.models import Forecast
from weather.providers.mock_weather_provider import MockWeatherProvider

VALID_API_KEY = "demo-key"


@pytest.fixture
def provider() -> MockWeatherProvider:
    return MockWeatherProvider(api_key=VALID_API_KEY)


@pytest.mark.parametrize(
    "expected",
    [
        Forecast(city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"),
        Forecast(city="Nairobi", temperature_celsius=22.0, condition="Light rain"),
        Forecast(city="Kampala", temperature_celsius=26.0, condition="Thunderstorms"),
    ],
)
def test_returns_forecast_for_known_city(
    provider: MockWeatherProvider, expected: Forecast
) -> None:
    assert provider.get_forecast(expected.city) == expected


def test_unknown_city_raises_city_not_found(provider: MockWeatherProvider) -> None:
    with pytest.raises(CityNotFoundError) as exc_info:
        provider.get_forecast("Atlantis")

    assert exc_info.value.city == "Atlantis"


@pytest.mark.parametrize("api_key", ["wrong-key", "", "DEMO-KEY"])
def test_invalid_api_key_raises(api_key: str) -> None:
    provider = MockWeatherProvider(api_key=api_key)

    with pytest.raises(InvalidAPIKeyError):
        provider.get_forecast("Kigali")


def test_api_key_is_checked_before_the_city() -> None:
    provider = MockWeatherProvider(api_key="wrong-key")

    with pytest.raises(InvalidAPIKeyError):
        provider.get_forecast("Atlantis")


@pytest.mark.parametrize("city", ["kigali", "KIGALI", "  Kigali  ", "kiGALi"])
def test_city_name_ignores_case_and_surrounding_spaces(
    provider: MockWeatherProvider, city: str
) -> None:
    assert provider.get_forecast(city).city == "Kigali"


@pytest.mark.parametrize("city", ["", "   "])
def test_blank_city_raises_city_not_found(
    provider: MockWeatherProvider, city: str
) -> None:
    with pytest.raises(CityNotFoundError):
        provider.get_forecast(city)


def test_unknown_city_is_logged_as_warning(
    provider: MockWeatherProvider, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level(logging.INFO), pytest.raises(CityNotFoundError):
        provider.get_forecast("Atlantis")

    assert "WARNING" in caplog.text
    assert "city not found city=Atlantis" in caplog.text


def test_rejected_key_is_logged_without_revealing_the_key(
    caplog: pytest.LogCaptureFixture,
) -> None:
    provider = MockWeatherProvider(api_key="secret-wrong-key")

    with caplog.at_level(logging.INFO), pytest.raises(InvalidAPIKeyError):
        provider.get_forecast("Kigali")

    assert "request rejected reason=invalid_api_key" in caplog.text
    assert "secret-wrong-key" not in caplog.text
