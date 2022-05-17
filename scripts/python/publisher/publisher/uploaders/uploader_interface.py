from abc import abstractmethod


class UploaderInterface:
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def upload(self):
        return
