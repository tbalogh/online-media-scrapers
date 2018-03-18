import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from .nynyny_archive_url_provider import NyNyNyArchiveUrlProvider

class TestNyNyNyArchiveUrlProvider:
    archiveUrlProvider = NyNyNyArchiveUrlProvider()

    def test_urls(self):
        test_map = {
            0: "https://888.hu/megtobbetszeretnek/?h=36",
            1: "https://888.hu/megtobbetszeretnek/?h=72",
            12: "https://888.hu/megtobbetszeretnek/?h=468",
        }

        for key, value in test_map.items():
            assert self.archiveUrlProvider.url(key) == value

    def test_provide_urls(self):
        test_map = {
            (0, 3): [
                "https://888.hu/megtobbetszeretnek/?h=36",
                "https://888.hu/megtobbetszeretnek/?h=72",
                "https://888.hu/megtobbetszeretnek/?h=108",
            ],
            (12, 2): [
                "https://888.hu/megtobbetszeretnek/?h=468",
                "https://888.hu/megtobbetszeretnek/?h=504",
            ],
            (0, 0): [],
            (723, 2): [
                "https://888.hu/megtobbetszeretnek/?h=26064",
                "https://888.hu/megtobbetszeretnek/?h=26100"
                ],
            (725, 1): []
        }

        for test_input, expected in test_map.items():
            i = 0
            for url in self.archiveUrlProvider.urls(test_input[0], test_input[1]):
                assert url == expected[i]
                i += 1
