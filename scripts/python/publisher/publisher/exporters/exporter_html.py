

from publisher.utility.utility_constructor import _init_parameter
import rich_click as click
from publisher.blogs.blog import Blog
from publisher.exporters.exporter_interface import ExporterInterface
import markdown

from publisher.logging.publisher_logger import get_logger

logger = get_logger()


class HtmlExporter(ExporterInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        _init_parameter(self, "extensions", kwargs, False)
        _init_parameter(self, "stylesheets", kwargs, False)

    def extend_cli(self, cli_group: click.Group):
        return super().extend_cli(cli_group)

    def export(self, blog: Blog, output_path: str):
        super().export(blog, output_path)
        blog_content = blog.content
        if blog_content is None:
            raise ValueError("The blog content is invalid or null")

        rendered_html = markdown.markdown(
            blog_content, extensions=self._extensions if hasattr(self, "_extensions") else [])

        if rendered_html is None:
            raise ValueError("The rendered HTML is invalid or null")
