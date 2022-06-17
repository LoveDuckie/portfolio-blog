
import typing


def _init_parameter(obj, parameter_name, parameters: dict, required: bool = False):
    if obj is None:
        raise ValueError("The object is invalid or null")

    if parameter_name is None:
        raise ValueError("The parameter name is invalid or null")

    if parameter_name not in parameters:
        raise KeyError(f"Failed to find the parameter {parameter_name}.")

    setattr(obj, parameter_name, parameters[parameter_name])
