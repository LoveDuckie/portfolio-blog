from typing import List
from publisher.logging.publisher_logger import get_logger
import rich_click as click

click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True


logger = get_logger()


@click.group()
def cli():
    pass


@click.command(name="Publish Blog", help="Publish the blog to the specified platforms.")
@click.option("--platform", '-p', multiple=True, type=click.Choice(['hashnode', 'dev.to']), type=str, help="The platforms to publish the blog to.")
@click.option("--blog", '-b', multiple=True, type=str, help="The slug names of the blogs to publish.")
def publish_blog(platform: List):
    pass


@click.command(name="Publish Collection", help="Publish a collection of blogs.")
@click.option("--collection", '-c', prompt=True, type=str, default=None, required=True, help="The name of the collection to publish.")
def publish_collection(collection: str):
    if collection is None:
        raise Exception(
            "The collection slug name was not defined. Unable to continue.")


@click.command(name="Configure Platform")
def configure_platform():
    pass


cli.add_command(publish_blog)
cli.add_command(publish_collection)
