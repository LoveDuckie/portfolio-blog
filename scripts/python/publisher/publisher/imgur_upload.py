from os import environ
import sys
import rich_click as click
import requests

from publisher.utility.utility_click import write_error, write_info
from publisher.utility.utility_config import get_config_property


def get_imgur_api_endpoint(*urls) -> str:
    url_combined = '/'.join(urls)
    return f"https://api.imgur.com/{url_combined}"


@click.group("imgur")
@click.option("--client-id", "-i", "client_id", default=get_config_property("publisher.image-uploader.imgur", "client-id"), prompt="Client ID", type=str, required=True, help="The client ID")
@click.option("--client-secret", "-s", "client_secret", default=get_config_property("publisher.image-uploader.imgur", "client-secret"), prompt="Client Secret", type=str, required=True, help="The client secret")
@click.pass_context
def cli(ctx, client_id: str, client_secret: str):
    ctx.ensure_object(dict)

    if client_id is None:
        raise ValueError("The client ID is none or invalid")
    if client_secret is None:
        raise ValueError("The client secret is none or invalid")
    ctx.obj["client_id"] = client_id
    ctx.obj["client_secret"] = client_secret


@cli.command("authorize")
@click.option("--pin", "-p", "pin", type=str, prompt="PIN", prompt_required=True, required=True)
@click.pass_context
def cli_authorize(ctx, pin: str):
    client_id: str = ctx.obj['client_id']
    client_secret: str = ctx.obj['client_secret']
    if not pin:
        raise ValueError("The PIN specified is invalid or null")
    api_url = get_imgur_api_endpoint("oauth2", "token")
    result = requests.post(api_url, json={
        "pin": pin,
        "grant_type": "pin",
        "client_id": client_id,
        "client_secret": client_secret
    })

    write_info(result.json())


@cli.command("authenticate")
@click.pass_context
def cli_authenticate(ctx):
    client_id: str = ctx.obj['client_id']
    client_secret: str = ctx.obj['client_secret']
    api_url = get_imgur_api_endpoint(
        "oauth2", "authorize", f"?response_type=pin&client_id={client_id}&client_secret={client_secret}")

    if not client_id:
        write_error("The client ID was not specified")
        return 1
    if not client_secret:
        write_error("The client secret was not specified")
        return 2

    click.launch(api_url)
    result = None
    while not (result := click.prompt("PIN")):
        write_error("PIN is invalid")

    # ctx.forward(cli_authorize)
    ctx.invoke(cli_authorize, pin=result)


@cli.command("upload")
@click.pass_context
def cli_upload(ctx):
    return

# @cli.result_callback()
# def process_pipeline(processors, input):
#     iterator = (x.rstrip('\r\n') for x in input)
#     for processor in processors:
#         iterator = processor(iterator)
#     for item in iterator:
#         click.echo(item)


if __name__ == "__main__":
    sys.exit(cli())
