

from publisher.blogs.blog import Blog
from publisher.exporters.exporter_interface import ExporterInterface
import markdown

from publisher.logging.publisher_logger import get_logger

logger = get_logger()


class HtmlExporter(ExporterInterface):
    def __init__(self, blog: Blog, *args, **kwargs) -> None:
        super().__init__(blog, *args, **kwargs)

    def export(self, output_path: str):
        super().export(output_path)

        if not hasattr(self, "blog"):
            raise ValueError(
                "Failed to find the blog attribute in the exporter")

        blog_content = self.blog.content

        rendered_html = markdown.markdown("", extensions=[])
        if rendered_html is None:
            raise ValueError("The rendered HTML is invalid or null")
