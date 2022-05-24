
import importlib
from typing import Any


def create_type_from_module_path(module_type_path: str, **kwargs) -> Any:
    """Instantiate the exporter from the type definition as a string

    Args:
        module_type_path (str): The fully qualified definition for the exporter type.

    Raises:
        ValueError: If the exporter type was not defined.
        ValueError: If it's not a fully qualified type declaration.
        ValueError: If the module instane is invalid.
        ValueError: If the exporter interface type was not retrievable from the module instance.

    Returns:
        ExporterInterface: The instantiated exporter.
    """
    if module_type_path is None:
        raise ValueError("The exporter type is invalid or null")

    if "." not in module_type_path:
        raise ValueError(
            "Full type definition is required for the exporter in order to create.")

    module_path_expanded = module_type_path.split('.')
    type_module = module_path_expanded[:-1]
    type_class_name = module_path_expanded[-1]

    if module_path_expanded is None:
        raise ValueError("Failed to expand the exporter type definition")

    type_module: str = '.'.join(module_type_path.split('.')[-1])

    type_module_instance = importlib.import_module(type_module)

    if not type_module_instance:
        raise ValueError("The module was not found")

    module_type = getattr(type_module_instance, type_class_name)
    if not module_type:
        raise ValueError("Failed to retrieve the interface type")

    module_type_instance = module_type(**kwargs)
    if module_type_instance is None:
        raise ValueError("The exporter instance is invalid or null")
    
    return module_type_instance