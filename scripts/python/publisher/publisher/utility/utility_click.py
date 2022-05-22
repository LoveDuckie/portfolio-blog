import rich_click as click


def write_info(msg, *fmt):
    click.echo(click.style(msg, fg='white'))


def write_debug(msg, *fmt):
    click.echo(click.style(msg, fg='white'))


def write_error(msg, *fmt):
    click.echo(click.style(msg, fg='red'))


def write_success(msg, *fmt):
    click.echo(click.style(msg, fg='green'))


def write_critical(msg, *fmt):
    click.echo(click.style(msg, bold=True, blink=True, bg='red', fg='white'))


def write_warning(msg, *fmt):
    click.echo(click.style(msg, fg='yellow'))
