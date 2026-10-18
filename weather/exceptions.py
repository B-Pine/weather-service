"""Custom exceptions raised by the weather service."""


class WeatherServiceError(Exception):
    """Base class for all weather service errors."""


class CityNotFoundError(WeatherServiceError):
    """Raised when no forecast exists for the requested city.

    Attributes:
        city: The city name that was requested.
    """

    def __init__(self, city: str) -> None:
        """Initialize the error with the requested city.

        Args:
            city: The city name that was requested.
        """
        super().__init__(f"City not found: '{city}'")
        self.city = city
