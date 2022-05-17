

from publisher.uploaders.uploader_interface import UploaderInterface


class HashNodeUploader(UploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upload(self):
        return super().upload()