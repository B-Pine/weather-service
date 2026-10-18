from weather.models import Forecast
from weather.services.weather_service import WeatherService


def test_get_forecast_returns_forecast_for_known_city() -> None:
    service = WeatherService()

    forecast = service.get_forecast("Kigali")

    assert forecast == Forecast(
        city="Kigali", temperature_celsius=24.0, condition="Partly cloudy"
    )
