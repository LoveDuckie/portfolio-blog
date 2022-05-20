import pkgutil
from typing import List
from publisher import exporters
import os


def _get_exporter_modules() -> List:
    return filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(exporters.__file__)]))


list(_get_exporter_modules())
