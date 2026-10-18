"""Forecast data model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Forecast:
    """The weather forecast for one city.

    Attributes:
        city: Name of the city the forecast is for.
        temperature_celsius: Expected temperature in degrees Celsius.
        condition: Short description of the weather, such as "Light rain".
    """

    city: str
    temperature_celsius: float
    condition: str
