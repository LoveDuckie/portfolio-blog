

from publisher.exporter.exporter_interface import ExporterInterface


class HashNodeExporter(ExporterInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
