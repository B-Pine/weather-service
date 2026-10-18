"""Text formatting helpers shared across the weather service."""


def normalize_city_name(name: str) -> str:
    """Reduce a city name to the form used for lookups.

    Args:
        name: A city name as typed, for example "  KIGALI ".

    Returns:
        The name without surrounding spaces and in lowercase, for
        example "kigali".
    """
    return name.strip().casefold()
