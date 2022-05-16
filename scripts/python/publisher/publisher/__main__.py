from typing import List
from publisher.logging.publisher_logger import get_logger
import rich_click as click


click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True


logger = get_logger()


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.group("configure")
@click.pass_context
def cli_configure(ctx):
    pass

@cli.group("blogs")
def cli_blogs(ctx):
    pass

@cli_blogs.command("create")
def cli_blogs_create(ctx):
    pass

@cli_blogs.command("delete")
def cli_blogs_delete(ctx):
    pass

@cli_blogs.command("list")
@click.option("--collection", default="default", type=str)
def cli_blogs_list(ctx):
    

@cli.group("collections")
def cli_collections(ctx):
    pass

@cli_collections.command("create")
@click.option("--name","-n",required=True, prompt=True, prompt_required=True, type=str)
def cli_collections_create(ctx):
    pass

@cli_configure.command("publisher")
@click.option("--set", type=str, required=True, prompt_required=True)
@click.pass_context
def cli_configure_publisher(set: str):
    return

@cli_configure.command("exporter")
@click.option("--parameter", '-p', type=str, required=True, prompt_required=True)
@click.pass_context
def cli_configure_exporter(parameter: str):
    
    return

@cli.group("publish")
@click.pass_context
def cli_publish(ctx):
    return

@cli.group("export", help="Export a blog to HTML or PDF format.")
@click.option("--exporter", type=str, help="The type of exporter to use")
@click.option("--path", type=str, help="The output path for the exporter (where relevant)")
@click.pass_context
def cli_export(ctx):
    return

@cli.command("publish-blog", help="Publish the blog to the specified platforms.")
@click.option("--platform", '-p', multiple=True, type=click.Choice(['hashnode', 'dev.to']), help="The platforms to publish the blog to.")
@click.option("--blog", '-b', multiple=True, type=str, help="The slug names of the blogs to publish.")
def publish_blog(platform: List, blog: str):
    for platform in platform:
        click.echo(platform)


@cli.command("publish-collection", help="Publish a collection of blogs.")
@click.option("--collection", '-c', prompt=True, type=str, default=None, required=True, help="The name of the collection to publish.")
def publish_collection(collection: str):
    if collection is None:
        raise Exception(
            "The collection slug name was not defined. Unable to continue.")


@click.command("configure-platform")
def configure_platform():
    pass


if __name__ == "__main__":
    cli()