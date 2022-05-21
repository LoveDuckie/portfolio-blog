import pkgutil
from typing import List
from publisher import exporters
import importlib
import os

from publisher.exporters.exporter_interface import ExporterInterface


def get_exporter_modules() -> List:
    return list(map(lambda x: x.name, filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(exporters.__file__)]))))


def create_exporter(exporter_type: str, **kwargs) -> ExporterInterface:
    if exporter_type is None:
        raise ValueError("The exporter type is invalid or null")

    if "." not in exporter_type:
        raise ValueError(
            "Full type definition is required for the exporter in order to create.")

    module_def: str = '.'.join(exporter_type.split('.')[:-1])
    module_instance = importlib.import_module(module_def)
    if not module_instance:
        raise ValueError("The module was not found")

    exporter_interface_type = getattr(module_instance, "")
    if not exporter_interface_type:
        raise ValueError("Failed to retrieve the interface type")
    return
