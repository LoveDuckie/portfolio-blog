

from abc import ABC, abstractmethod
import os
from typing import List

from publisher.blogs.blog import Blog
from publisher.utility.utility_constructor import _init_parameter
import rich_click as click


class ExporterInterface(ABC):
    def __init__(self, *args, **kwargs) -> None:
        _init_parameter(self, "assets", kwargs)

    @property
    def blog(self):
        return self._blog

    def assets(self) -> List:
        return []

    @abstractmethod
    def export(self, blog: Blog, output_path: str):

        if not output_path:
            raise ValueError("The output path is invalid or null")

        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if blog is None:
            raise ValueError("The blog is invalid or null")

    @abstractmethod
    def extend_cli(self, cli_group: click.Group):
        if cli_group is None:
            raise ValueError("The cli group is invalid or null")
