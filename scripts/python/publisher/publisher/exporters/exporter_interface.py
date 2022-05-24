

from abc import abstractmethod
from typing import List

from publisher.blogs.blog import Blog


class ExporterInterface:
    def __init__(self, blog: Blog, *args, **kwargs) -> None:
        if blog is None:
            raise ValueError("The blog is ivnalid or null")
        if "assets" in kwargs:
            self.assets = kwargs['assets']
        self._blog = blog

    @property
    def blog(self):
        return self._blog

    def assets(self) -> List:
        return []

    @abstractmethod
    def export(self, output_path: str):
        if not hasattr(self, "blog"):
            raise AttributeError("blog is no defined")
        if output_path is None:
            raise ValueError("The target output path is invalid or null")
        return
