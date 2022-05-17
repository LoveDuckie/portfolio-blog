

from abc import abstractmethod


class ImageUploaderInterface:
    def __init__(self, *args, **kwargs) -> None:
        pass
    
    @abstractmethod
    def upload(self):
        return