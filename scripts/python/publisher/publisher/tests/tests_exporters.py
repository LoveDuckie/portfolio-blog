import unittest

from publisher.utility.utility_exporters import get_exporter_modules


class TestsExporters(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_create_exporters(self):
        exporters = get_exporter_modules()
        self.assertTrue(exporters is not None)
        for _ in exporters:
            continue

    def test_exporter_html(self):
        pass

    def test_exporter_silverstripe(self):
        pass

    def test_exporters_available(self):
        exporters = get_exporter_modules()
        self.assertTrue(any(exporters))


if __name__ == '__main__':
    unittest.main()
