import pkgutil
from typing import List
from publisher import exporters
import os

from publisher.exporters.exporter_interface import ExporterInterface


def get_exporter_modules() -> List:
    return list(map(lambda x: x.name, filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(exporters.__file__)]))))


def create_exporter(exporter_type: str) -> ExporterInterface:
    if exporter_type is None:
        raise ValueError("The exporter type is invalid or null")
    
    if not "." in exporter_type:
        pass
    return