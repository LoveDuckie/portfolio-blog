from publisher.uploaders.uploader_interface import UploaderInterface

import click as rich_click

class DevToUploader(UploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    async def upload(self, content: str):
        return super().upload(content)
    
    def extend_cli(self, cli_group: click.Group):
        return super().extend_cli(cli_group)