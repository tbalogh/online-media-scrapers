import sys, os
sys.path.append(os.path.dirname(os.path.relpath(__file__)))

import unittest
from ps_archive_url_provider import PsArchiveUrlProvider

class TestPsArchiveUrlProvider(unittest.TestCase):
    archiveUrlProvider = PsArchiveUrlProvider()

    def test_urls(self):
        test_map = {
            0: "http://pestisracok.hu",
            2: "http://pestisracok.hu/page/2",
            83: "http://pestisracok.hu/page/83"
        }
        for key, value in test_map.items():
            assert self.archiveUrlProvider.url(key) == value

    def test_provide_ps_urls(self):
        test_map = {
            (0, 3): [
                "http://pestisracok.hu",
                "http://pestisracok.hu/page/1",
                "http://pestisracok.hu/page/2",
                "http://pestisracok.hu/page/3"
            ],
            (12, 13): [
                "http://pestisracok.hu/page/12",
                "http://pestisracok.hu/page/13",
            ],
            (50, 51): [
                "http://pestisracok.hu/page/50",
                "http://pestisracok.hu/page/51",
            ],
            (0, 0): [
            ]
        }
        for (start_idx, num_of_pages), expected in test_map.items():
            i = 0
            urls = list(self.archiveUrlProvider.urls(start_idx, num_of_pages))
            print(urls)
            self.assertListEqual(expected, urls)
                
