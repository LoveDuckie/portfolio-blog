from publisher.exporter.exporter_interface import ExporterInterface


class SilverstripeExporter(ExporterInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def export(self):
        return super().export()