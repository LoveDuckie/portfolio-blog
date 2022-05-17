

from publisher.blogs.blog import Blog
from publisher.decorators.exporters.decorators_exporter import exporter
from publisher.exporters.exporter_interface import ExporterInterface


@exporter(name="Silverstripe Exporter", description="Custom Exporter for Silverstripe")
class SilverstripeExporter(ExporterInterface):
    def __init__(self, blog: Blog) -> None:
        super().__init__(blog)

    def export(self):
        return super().export()
