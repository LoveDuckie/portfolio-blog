from abc import abstractmethod


class ExporterInterface:
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def export(self):
        return
