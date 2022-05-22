import os
import sys
from typing import List
from publisher.logging.publisher_logger import get_logger
import traceback
import rich_click as click
from publisher.utility.utility_blogs import create_blog, get_blogs, is_valid_collection
from publisher.utility.utility_click import write_error, write_info, write_success
from publisher.utility.utility_exporters import get_exporter_modules
from publisher.utility.utility_names import create_slug_from_name
from publisher.utility.utility_paths import get_default_collection_name, get_default_collections_path


click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True

logger = get_logger()


def validate_parameter(ctx, param, value):
    if param is None:
        raise ValueError("The parameter specified is invalid or null")
    if value is None:
        raise ValueError("The value specified is invalid or null")
    return


def validate_blog(ctx, param, value):
    if ctx is None:
        raise ValueError("The context object is invalid or null")
    if param is None:
        raise ValueError("The parameter specified is invalid or null")
    if value is None:
        raise ValueError("The value specified is invalid or null")
    return


def validate_collection(ctx, param, value):
    if param is None:
        raise ValueError("The parameter specified is invalid or null")
    if value is None:
        raise ValueError("The value specified is invalid or null")
    return


@click.group(help="The command-line interface for the Publisher tool.")
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)

@cli.group("config", help="Modify the behaviour of the publisher tool.")
@click.pass_context
def cli_config(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli.group("tests", help="Run any of the available unit tests.")
def cli_tests(ctx):
    if ctx is None:
        raise ValueError("The context object is invalid or null")


@cli_tests.command("list", help="List all available tests that can be used")
@click.option("--tests-path", type=str, help="The absolute path to where unit tests are defined.")
def cli_tests_list(ctx, tests_path: str):
    if not tests_path:
        raise ValueError("The tests path is invalid or null")

    if not os.path.isabs(tests_path):
        pass
    return


@cli_config.command("show", help="Show the current configuration values.")
@click.option("--collection-id", "-c", "collection_id", type=str, default=get_default_collection_name(), help="The name of the collection to reveal configuration information about")
@click.pass_context
def cli_config_show(ctx, collection_id: str):
    write_info(f"Collections Path: {get_default_collections_path()}")
    if collection_id is not None and not is_valid_collection(collection_id):
        write_error(f"The collection \"{collection_id}\" is not valid.")
    write_success("Done")


@cli.group("blogs", help="Manage singular blogs.")
@click.option("--collection-id", "-c", "collection_id", type=str, required=False, default=get_default_collection_name(), help="The slug ID of the blog collection")
@click.pass_context
def cli_blogs(ctx, collection_id: str):
    ctx.ensure_object(dict)
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    ctx.obj['collection_id'] = collection_id


@cli_blogs.command("create", help="Create a new blog in a collection.")
@click.option("--blog-id", type=str, default=None, required=True, prompt_required=True, prompt="Blog Name", help="The name of the blog to create.")
@click.pass_context
def cli_blogs_create(ctx, blog_name: str):
    if blog_name is None:
        raise ValueError(
            "The name of the blog is invalid or null. Unable to continue.")

    collection_id: str = ctx.obj['collection_id']
    blog_id: str = create_slug_from_name(blog_name)
    write_info(f"Creating: \"{blog_id}\"")
    try:
        create_blog(blog_id, collection_id)
    except Exception:
        tb = traceback.format_exc()
        write_error(tb)

    write_success("Done")


@cli_blogs.command("open", help="Open an existing blog from the collection specified.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The slug ID of the blog")
@click.pass_context
def cli_blogs_create(ctx, blog_id: str):
    if blog_id is None:
        raise ValueError("The blog I specified is invalid or null")

    write_success("Done")
    return 1


@cli_blogs.command("delete", help="Delete an existing blog from a collection.")
@click.option("--blog-id", "-b", "blog_id", type=str, required=True, help="The slug ID of the blog")
@click.pass_context
def cli_blogs_delete(ctx, blog_id: str):
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    write_success("Done")
    return 1


@cli_blogs.command("list", help="List all blogs.")
@click.pass_context
def cli_blogs_list(ctx):
    collection_id = ctx.obj['collection_id']
    blogs = get_blogs(collection_id)

    if not blogs:
        raise ValueError("The blogs found are invalid or null")

    write_info(f"Blogs found in collection \"{collection_id}\"")
    for blog in blogs:
        write_info(f"Blog: \"{blog.name}\"")

    write_success("Done")
    return 0


@cli.group("collections", help="Manage collections of blogs.")
@click.option("--path", "-p", "path", type=str, required=False, default=get_default_collections_path(), help="The absolute path to where collections are stored.")
@click.pass_context
def cli_collections(ctx, path: str):
    ctx.ensure_object(dict)
    if not path:
        raise ValueError("The path is invalid or null")

    ctx.obj['collections_path'] = path
    return 0


@cli_collections.command("list", help="List all the collections.")
@click.option("--short", "-s", "short", is_flag=True, required=False, help="Display a shorter output from the list of collections.")
@click.pass_context
def cli_collections_list(ctx, short: bool):
    collections_path = ctx.obj['collections_path']
    if collections_path is None:
        raise ValueError(
            "The collections path is invalid or null. Unable to continue.")

    write_success("Done")


@cli_collections.command("delete", help="Delete the collections specified.")
@click.option("--name", "-n", "names", type=str, multiple=True, required=True, help="The slug ID(s) of he collection(s) to delete.")
@click.pass_context
def cli_collections_delete(ctx, names: List[str]):
    if not names:
        raise ValueError("The names specified are invalid or null")


@cli_collections.command("create", help="Create the collection specified.")
@click.option("--name", "-n", "names", required=True, prompt=True, prompt_required=True, multiple=True, type=str, help="The name(s) of the collection to create.")
def cli_collections_create(ctx, names: List[str]):
    if names is None:
        raise ValueError("The name is invalid or null")

    collection_slug_name = create_slug_from_name(names)

    if is_valid_collection(collection_slug_name):
        write_error(f"The collection \"{names}\" already exists")
        return 1

    write_success("Done")


@cli_config.command("publisher")
@click.option("--set", '-s', "parameters", type=str, required=True, prompt_required=True, help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_publisher(parameters: List[str]):
    for parameter in parameters:
        write_info(parameter)
    write_success("Done")


@cli_config.command("exporter")
@click.option("--type", "-t", type=str, help="The absolute type path for the exporter.")
@click.option("--set", '-s', "parameters", type=str, required=True, prompt_required=True, help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_exporter(parameters: List[str]):
    for parameter in parameters:
        write_info(parameter)
    write_success("Done")


@cli_config.command("uploader")
@click.option("--type", "-t", type=str, help="The absolute type path for the uploader.")
@click.option("--set", '-s', "parameters", type=str, required=True, prompt_required=True, default=[], help="The parameters to set, as key/value pairs.")
@click.pass_context
def cli_config_exporter(parameters: List[str]):
    # sourcery skip: raise-specific-error
    if parameters is None:
        raise ValueError("The parameters are invalid or null")
    if not any(parameters):
        raise Exception("No parameters were found.")
    return


@cli.group("upload", help="Upload a collection of blogs or a single blog.")
@click.pass_context
def cli_upload(ctx):
    ctx.ensure_object(dict)
    return


@cli_upload.command("blog", help="Upload a blog.")
@click.option("--name", "-n", "name", type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option("--collection-id", "-c", "collection_id", type=str, default="default", required=True, prompt=True, prompt_required=True)
@click.pass_context
def cli_upload_blog(ctx, name: str, collection: str):
    return


@cli_upload.command("collection", help="Upload a collection.")
@click.option('--name', '-n', type=str, default=None, required=True, prompt=True, prompt_required=True)
@click.option('--collections-path', '-c', 'collections_path', type=str, default=get_default_collections_path(), required=False, prompt=True, prompt_required=True)
@click.pass_context
def cli_upload_collection(ctx, collections_path: str):
    if collections_path is None:
        raise ValueError("The collections path specified is invalid or null")


@cli.group("export", help="Render the blog out to a path specified.")
@click.option("--exporter", type=click.Choice(get_exporter_modules(), case_sensitive=True), help="The type qualification for the exporter to use.")
@click.option("--force", "-f", "force", is_flag=True, help="Overwrite the blog if there's one already.")
@click.option("--path", "-p", "path", type=str, help="The output path for the exporter (where relevant).")
@click.pass_context
def cli_export(ctx, exporter: str, force: bool, path: str):
    ctx.ensure_object(dict)


if __name__ == "__main__":
    sys.exit(cli())
