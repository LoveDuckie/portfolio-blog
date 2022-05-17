from publisher.logging.publisher_logger import get_logger
import rich_click as click
from publisher.utility.utility_blogs import is_valid_collection, create_slug_from_name


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
    pass


@cli.group("collections")
def cli_collections(ctx):
    pass


@cli_collections.command("create")
@click.option("--name", "-n", required=True, prompt=True, prompt_required=True, type=str)
def cli_collections_create(ctx, name: str):
    if name is None:
        raise ValueError("The name is invalid or null")

    collection_slug_name = create_slug_from_name(name)
    if is_valid_collection(collection_slug_name):
        click.echo(f"The collection \"{name}\" already exists")


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


@cli.group("upload")
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
@click.option("--path", type=str, help="The output path for the exporter (where relevant)")
@click.pass_context
def cli_export(ctx):
    return



if __name__ == "__main__":
    cli()
