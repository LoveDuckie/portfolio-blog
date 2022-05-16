from publisher.exporter.exporter_interface import ExporterInterface


class DevToExporter(ExporterInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)