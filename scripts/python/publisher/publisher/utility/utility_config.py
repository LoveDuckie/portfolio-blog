from configparser import ConfigParser
from typing import Any, List

from publisher.utility.utility_paths import get_default_config_filepath, get_default_user_config_filepath

config_env_map = None


def _get_config_env_map() -> dict[str, str]:
    global config_env_map
    if config_env_map is not None:
        return config_env_map
    return {}


def _get_config() -> ConfigParser:
    config_parser = ConfigParser()
    config_parser.read(get_default_config_filepath())
    return config_parser


def _get_user_config() -> ConfigParser:
    config_parser = ConfigParser()
    config_parser.read(get_default_user_config_filepath())
    return config_parser


def get_config_section_properties(property_section: str) -> List:
    if property_section is None:
        raise ValueError("The property section is invalid or null")


def has_config_property(property_section: str, property_name: str) -> bool:
    """Determine whether the configuration property exists in the section specified.

    Args:
        property_section (str): The section that contains the property.
        property_name (str): The name of the property.

    Raises:
        ValueError: If the property section is null or invalid.
        ValueError: If the property name is invalid or null.
        ValueError: If the loaded configuration object is valid or null.

    Returns:
        bool: _description_
    """
    if property_section is None:
        raise ValueError("The property section is invalid or null")
    if property_name is None:
        raise ValueError("The property name is invalid or null")

    config_parser = _get_config()
    if config_parser is None:
        raise ValueError("The configuration parser is invalid or null")

    if property_section not in config_parser:
        return False

    if property_name not in config_parser[property_section]:
        return False

    return True


def get_user_config_property(property_section: str, property_name: str) -> str:
    """Get the property value from the section specified in the user configuration.

    Args:
        property_section (str): The property section.
        property_name (str): The name of the property.

    Raises:
        ValueError: The property section is invalid or null.
        ValueError: The property name is invalid or null.
        ValueError: The configuration property does not exist.

    Returns:
        str: Returns the stored configuration property value.
    """
    if property_section is None:
        raise ValueError("The property section is invalid or null")
    if property_name is None:
        raise ValueError("The property name is invalid or null")

    if not has_config_property(property_section, property_name):
        raise ValueError(
            f"Unable to find the configuration value \"{property_section}.{property_name}\"")

    config = _get_user_config()
    return config[property_section][property_name]


def get_config_property(property_section: str, property_name: str) -> Any:
    if property_section is None:
        raise ValueError("The property section is invalid or null")
    if property_name is None:
        raise ValueError("The property name is invalid or null")

    if not has_config_property(property_section, property_name):
        raise ValueError(
            f"Unable to find the configuration value \"{property_section}.{property_name}\"")

    config = _get_config()
    return config[property_section][property_name]
