import pkgutil
from typing import List
from publisher import exporters
import importlib
import os

from publisher.exporters.exporter_interface import ExporterInterface


def get_exporter_modules_map() -> dict[str, str]:
    return {}


def get_exporter_modules() -> List[str]:
    return list(map(lambda x: x.name, filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(exporters.__file__)]))))


def is_valid_exporter(exporter_id: str) -> bool:
    if exporter_id is None:
        raise ValueError("The exporter ID is invalid or null")

    return False


def create_exporter(exporter_type: str, **kwargs) -> ExporterInterface:
    """Instantiate the exporter from the type definition as a string

    Args:
        exporter_type (str): The fully qualified definition for the exporter type.

    Raises:
        ValueError: If the exporter type was not defined.
        ValueError: If it's not a fully qualified type declaration.
        ValueError: If the module instane is invalid.
        ValueError: If the exporter interface type was not retrievable from the module instance.

    Returns:
        ExporterInterface: The instantiated exporter.
    """
    if exporter_type is None:
        raise ValueError("The exporter type is invalid or null")

    if "." not in exporter_type:
        raise ValueError(
            "Full type definition is required for the exporter in order to create.")

    exporter_type_expanded = exporter_type.split('.')
    exporter_type_module = exporter_type_expanded[:-1]
    exporter_type_class = exporter_type_expanded[-1]

    if exporter_type_expanded is None:
        raise ValueError("Failed to expand the exporter type definition")

    exporter_type_module: str = '.'.join(exporter_type.split('.')[-1])

    exporter_module_instance = importlib.import_module(exporter_type_module)

    if not exporter_module_instance:
        raise ValueError("The module was not found")

    exporter_type = getattr(exporter_module_instance, exporter_type_class)
    if not exporter_type:
        raise ValueError("Failed to retrieve the interface type")

    exporter_type_instance = exporter_type(**kwargs)
    if exporter_type_instance is None:
        raise ValueError("The exporter instance is invalid or null")
    
    return exporter_type_instance
