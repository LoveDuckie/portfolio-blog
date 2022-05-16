

from publisher.blogs.blog import Blog
from publisher.exporter.exporter_interface import ExporterInterface


class SilverstripeExporter(ExporterInterface):
    def __init__(self, blog: Blog) -> None:
        super().__init__(blog)
        
    def export(self):
        return super().export()