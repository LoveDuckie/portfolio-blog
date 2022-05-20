from abc import abstractmethod


class UploaderInterface:
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def upload(self, content: str):
        if content is None:
            raise ValueError("The content is invalid or null")
        return
