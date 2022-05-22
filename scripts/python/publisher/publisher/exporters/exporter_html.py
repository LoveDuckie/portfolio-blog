

from publisher.blogs.blog import Blog
from publisher.exporters.exporter_interface import ExporterInterface
import markdown

from publisher.logging.publisher_logger import get_logger

logger = get_logger()

class HtmlExporter(ExporterInterface):
    def __init__(self, blog: Blog, *args, **kwargs) -> None:
        params = ['stylesheets']
        for key in kwargs:
            if key in params:
                setattr(self, key, kwargs[key])
        super().__init__(blog)
        
    def export(self, target_output_path: str):
        super().export(target_output_path)

        if not hasattr(self,"blog"):
            raise ValueError("Failed to find the blog attribute in the exporter")

        rendered_html = markdown.markdown("",extensions=[])
        if rendered_html is None:
            raise ValueError("")