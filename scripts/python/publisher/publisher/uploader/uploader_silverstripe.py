from publisher.uploader.uploader_interface import UploaderInterface


class SilverstripeUploader(UploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def export(self):
        return super().export()