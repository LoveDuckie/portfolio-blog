

from publisher.image_uploaders.image_uploader_interface import ImageUploaderInterface


class SilverStripeImageUploader(ImageUploaderInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def requires_authentication(self) -> bool:
        return super().requires_authentication

    def authenticate(self):
        return super().authenticate()

    def upload(self, target_filepath: str):
        return super().upload(target_filepath)
