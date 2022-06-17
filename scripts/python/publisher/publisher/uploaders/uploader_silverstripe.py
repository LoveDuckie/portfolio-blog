from publisher.uploaders.uploader_interface import UploaderInterface


class SilverstripeUploader(UploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def upload(self, content: str):
        return super().export()
