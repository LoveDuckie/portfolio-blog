from abc import ABC, abstractmethod

import rich_click as click

class UploaderInterface(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def upload(self, content: str, **kwargs):
        if content is None:
            raise ValueError("The content is invalid or null")
        return

    @abstractmethod
    def extend_cli(self, cli_group: click.Group):
        if cli_group is None:
            raise ValueError("The cli group is invalid or null")