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


class InvalidAPIKeyError(WeatherServiceError):
    """Raised when the API key is not accepted.

    The key itself is never included in the message, so it cannot leak
    into logs or error reports.
    """

    def __init__(self) -> None:
        """Initialize the error with a fixed message."""
        super().__init__("Invalid API key")
