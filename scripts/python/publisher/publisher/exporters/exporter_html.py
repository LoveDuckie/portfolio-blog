

from publisher.blogs.blog import Blog
from publisher.exporters.exporter_interface import ExporterInterface
import markdown


class HtmlExporter(ExporterInterface):
    def __init__(self, blog: Blog) -> None:
        super().__init__(blog)
        
    def export(self):
        if not hasattr(self, "blog"):
            raise AttributeError("blog is no defined")
        markdown.markdown()
        return super().export()