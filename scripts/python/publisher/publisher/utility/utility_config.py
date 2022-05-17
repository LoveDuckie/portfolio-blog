from multiprocessing.sharedctypes import Value
import os
import sys
from configparser import ConfigParser
from typing import Any

from publisher.utility.utility_paths import get_default_config_filepath, get_default_user_config_filepath


def _get_config() -> ConfigParser:
    config_parser = ConfigParser()
    config_parser.read(get_default_config_filepath())
    return config_parser


def _get_user_configg() -> ConfigParser:
    config_parser = ConfigParser()
    config_parser.read(get_default_user_config_filepath())
    return config_parser


def has_config_property(property_section: str, property_name: str) -> bool:
    if property_section is None:
        raise ValueError("The property section is ivnalid or null")
    if property_name is None:
        raise ValueError("The property section is ivnalid or null")

    config_parser = _get_config()
    if config_parser is None:
        raise ValueError("The configuration parser is invalid or null")

    if property_section not in config_parser:
        return False

    if property_name not in config_parser[property_section]:
        return False

    return True


def get_config_property(property_section: str, property_name: str) -> Any:
    if property_section is None:
        raise ValueError("The property section is ivnalid or null")
    if property_name is None:
        raise ValueError("The property section is ivnalid or null")

    if not has_config_property(property_section, property_name):
        raise ValueError(
            f"Unable to find the configuration value \"{property_section}.{property_name}\"")

    config = _get_config()
