import os
import sys
from time import sleep
from publisher.logging.publisher_logger import get_logger
import rich_click as click
from publisher.utility.utility_blogs import is_valid_collection
from publisher.utility.utility_click import write_error
from publisher.utility.utility_names import create_slug_from_name
from publisher.utility.utility_paths import get_default_collection_name, get_default_collections_path


click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True


logger = get_logger()


@click.group(help="The command-line interface for the Publisher tool.")
@click.pass_context
def cli(ctx):
    pass


@cli.group("configure", help="Modify the behaviour of the publisher tool.")
@click.pass_context
def cli_configure(ctx):
    pass


@cli.group("blogs", help="Manage singular blogs")
@click.option("--collection", "-c", "collection", type=str, required=False, default=get_default_collection_name(), help="The slug ID of the blog collection")
@click.pass_context
def cli_blogs(ctx, collection: str):
    if collection is None:
        raise ValueError("The collection ID is invalid or null")


@cli_blogs.command("create", help="Create a new blog in a collection")
@click.pass_context
def cli_blogs_create(ctx):
    pass


@cli_blogs.command("delete")
@click.option("--blog", "-b", "blog", type=str, required=True, help="The slug ID of the blog")
@click.pass_context
def cli_blogs_delete(ctx, blog: str):
    if blog is None:
        raise ValueError("The blog specified is invalid or null")


@cli_blogs.command("list", help="List all blogs.")
@click.pass_context
def cli_blogs_list(ctx):
    pass


@cli.group("collections", help="Manage collections of blogs.")
@click.pass_context
def cli_collections(ctx):
    pass


@cli_collections.command("list", help="List all the collections")
@click.option("--short", "-s", "short", is_flag=True, required=False, help="Display a shorter output from the list of collections")
@click.pass_context
def cli_collections_list(ctx, short: bool):
    pass


@cli_collections.command("delete", help="Delete a single collection.")
@click.option("--name", "-n", "name", type=str, required=True, help="The slug ID of he collection to delete")
@click.pass_context
def cli_collections_delete(ctx):
    pass


@cli_collections.command("create")
@click.option("--name", "-n", required=True, prompt=True, prompt_required=True, type=str)
def cli_collections_create(ctx, name: str):
    if name is None:
        raise ValueError("The name is invalid or null")

    collection_slug_name = create_slug_from_name(name)
    if is_valid_collection(collection_slug_name):
        write_error(f"The collection \"{name}\" already exists")
        return 1


@cli_configure.command("publisher")
@click.option("--set", type=str, required=True, prompt_required=True)
@click.pass_context
def cli_configure_publisher(set: str):
    return


@cli_configure.command("exporter")
@click.option("--type", "-t", type=str, help="The absolute type path for the exporter.")
@click.option("--parameter", '-p', type=str, required=True, prompt_required=True)
@click.pass_context
def cli_configure_exporter(parameter: str):
    return


@cli_configure.command("uploader")
@click.option("--parameter", '-p', type=str, required=True, prompt_required=True)
@click.pass_context
def cli_configure_exporter(parameter: str):
    return


@cli.group("upload", help="Upload a collection of blogs or a single blog.")
@click.pass_context
def cli_upload(ctx):
    return


def validate_blog(ctx, value):
    return


def validate_collection(ctx, value):
    return


@cli_upload.command("blog", help="Upload a blog.")
@click.option('--name', '-n', type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option('--collection', '-c', type=str, default="default", required=True, prompt=True, prompt_required=True)
@click.pass_context
def cli_upload_blog(ctx):
    return


@cli_upload.command("collection", help="Upload a collection.")
@click.option('--name', '-n', type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.pass_context
def cli_upload_collection(ctx):
    return


@cli.group("export", help="Render the blog to some kind of format.")
@click.option("--exporter", type=str, help="The type of exporter to use")
@click.option("--force", "-f", "force", is_flag=True, help="The type of exporter to use")
@click.option("--path", type=str, help="The output path for the exporter (where relevant)")
@click.pass_context
def cli_export(ctx):
    return


if __name__ == "__main__":
    sys.exit(cli())
