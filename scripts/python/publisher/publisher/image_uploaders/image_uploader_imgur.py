

from publisher.image_uploaders.image_uploader_interface import ImageUploaderInterface


class ImgurImageUploader(ImageUploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upload(self):
        super().upload()
