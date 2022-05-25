

from publisher.image_uploaders.image_uploader_interface import ImageUploaderInterface


class SilverStripeImageUploader(ImageUploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upload(self, target_filepath: str):
        return super().upload(target_filepath)
