from publisher.uploaders.uploader_interface import UploaderInterface
import rich_click as click

def get_medium_api_url(*urls) -> str:
    urls_combined: str = '/'.join(urls)
    return f"https://api.medium.com/v1/{urls_combined}"


class MediumUploader(UploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def upload(self, content: str):
        return super().upload()

    def extend_cli(self, cli_group: click.Group):
        return super().extend_cli(cli_group)