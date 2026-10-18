import logging
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from weather.models import Forecast
from weather.providers.mock_weather_provider import MockWeatherProvider
from weather.providers.weather_provider import WeatherProvider
from weather.services.weather_service import WeatherService

TESTVILLE = Forecast(city="Testville", temperature_celsius=-5.0, condition="Snow")


@pytest.fixture
def provider(mocker: MockerFixture) -> MagicMock:
    mock: MagicMock = mocker.create_autospec(WeatherProvider, instance=True)
    mock.get_forecast.return_value = TESTVILLE
    return mock


@pytest.fixture
def service(provider: MagicMock) -> WeatherService:
    return WeatherService(provider=provider)


def test_forecast_comes_from_the_injected_provider(
    service: WeatherService, provider: MagicMock
) -> None:
    forecast = service.get_forecast("Testville")

    assert forecast == TESTVILLE
    provider.get_forecast.assert_called_once_with("Testville")


def test_successful_request_is_logged(
    service: WeatherService, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level(logging.INFO):
        service.get_forecast("Testville")

    assert "forecast requested city=Testville" in caplog.text
    assert "forecast returned city=Testville condition=Snow" in caplog.text


def test_works_with_the_mock_provider() -> None:
    service = WeatherService(provider=MockWeatherProvider(api_key="demo-key"))

    assert service.get_forecast("Kigali").condition == "Partly cloudy"
